#!/usr/bin/env python

import os
from collections import defaultdict
from urllib.parse import urlparse

import fire
import requests

from .encoder import Encoder


class Client:
    output_style = "json"

    def __init__(
        self,
        api_token=None,
        host=None,
        proto=None,
        ssl_cert_verify=None,
        output_style=None,
    ):
        if output_style:
            self.output_style = output_style
        self.host = host if host else os.environ.get("ANOMALO_INSTANCE_HOST")
        self.api_token = (
            api_token if api_token else os.environ.get("ANOMALO_API_SECRET_TOKEN")
        )

        if not self.host:
            raise RuntimeError(
                "Please specify Anomalo instance host via ANOMALO_INSTANCE_HOST env var"
            )
        if not self.api_token:
            raise RuntimeError(
                "Please specify Anomalo api token via ANOMALO_API_SECRET_TOKEN env var"
            )

        parsed_host_url = urlparse(self.host)
        host_scheme = parsed_host_url.scheme
        if host_scheme:
            self.proto = host_scheme
            self.host = parsed_host_url.netloc
        else:
            self.proto = proto if proto else "https"

        self.request_headers = {"X-Anomalo-Token": self.api_token}

        self.verify = ssl_cert_verify

    def _api_call(self, endpoint, method="GET", **kwargs):

        endpoint_url = "{proto}://{host}/api/public/v1/{endpoint}".format(
            proto=self.proto, host=self.host, endpoint=endpoint
        )

        if method in ["PUT", "POST"]:
            request_args = dict(json=kwargs)
        else:
            request_args = dict(params=kwargs)
        r = requests.request(
            method,
            endpoint_url,
            headers=self.request_headers,
            verify=self.verify,
            allow_redirects=False,
            **request_args,
        )

        if not r.ok:
            raise RuntimeError(r.text)
        return r.json() if self.output_style == "json" else r.text

    def ping(self):
        return self._api_call("ping")

    def get_active_organization_id(self):
        return self._api_call("organization").get("id")

    def set_active_organization_id(self, organization_id):
        return self._api_call("organization", method="PUT", id=organization_id).get(
            "id"
        )

    def get_all_organizations(self):
        return self._api_call("organizations")

    def list_warehouses(self):
        return self._api_call("list_warehouses")

    def refresh_warehouse(self, warehouse_id):
        return self._api_call(f"warehouse/{warehouse_id}/refresh", method="PUT")

    def refresh_warehouse_tables(self, warehouse_id, table_full_names):
        if not table_full_names:
            raise RuntimeError("Must specify a list of full table names to sync")
        return self._api_call(
            f"warehouse/{warehouse_id}/refresh",
            method="PUT",
            table_full_names=table_full_names,
        )

    def refresh_warehouse_new_tables(self, warehouse_id):
        return self._api_call(f"warehouse/{warehouse_id}/refresh/new", method="PUT")

    def list_notification_channels(self):
        return self._api_call("list_notification_channels")

    def configured_tables(self, check_cadence_type=None, warehouse_id=None):
        return self._api_call(
            "configured_tables",
            check_cadence_type=check_cadence_type,
            warehouse_id=warehouse_id,
        )

    def get_table_information(self, warehouse_id=None, table_id=None, table_name=None):
        if (not table_id or not warehouse_id) and not table_name:
            raise RuntimeError(
                "Must specify either warehouse_id & table_id or table_name for get_table_information"
            )
        else:
            return self._api_call(
                "get_table_information",
                warehouse_id=warehouse_id,
                table_id=table_id,
                table_name=table_name,
            )

    def get_check_intervals(self, table_id=None, start=None, end=None):
        if not table_id:
            raise RuntimeError("Must specify a table_id for get_check_intervals")
        else:
            results = []
            page = 0
            paged_results = None
            while paged_results is None or len(paged_results) > 0:
                paged_results = self._api_call(
                    "get_check_intervals",
                    table_id=table_id,
                    start=start,
                    end=end,
                    page=page,
                )["intervals"]
                results.extend(paged_results)
                page = page + 1
            return results

    def get_checks_for_table(self, table_id):
        return self._api_call("get_checks_for_table", table_id=table_id)

    def run_checks(self, table_id, interval_id=None, check_ids=None):
        if check_ids:
            if not isinstance(check_ids, list) and not isinstance(check_ids, tuple):
                check_ids = [check_ids]
            check_ids = list(check_ids)  # Convert from Tuple
            return self._api_call(
                "run_checks",
                method="POST",
                table_id=table_id,
                interval_id=interval_id,
                check_ids=check_ids,
            )
        else:
            return self._api_call(
                "run_checks",
                method="POST",
                table_id=table_id,
                interval_id=interval_id,
            )

    def get_run_result(self, job_id):
        return self._api_call("get_run_result", run_checks_job_id=job_id)

    def get_run_result_triage_history(self, job_id):
        return self._api_call("get_run_result_triage_history", run_checks_job_id=job_id)

    def create_check(self, table_id, check_type, **params):
        return self._api_call(
            "create_check",
            table_id=table_id,
            check_type=check_type,
            method="POST",
            params=params,
        )

    def delete_check(self, table_id, check_id):
        return self._api_call(
            "delete_check",
            table_id=table_id,
            check_id=check_id,
            method="POST",
        )

    def clone_check(self, table_id, check_id, new_table_id):
        return self._api_call(
            "clone_check",
            table_id=table_id,
            check_id=check_id,
            new_table_id=new_table_id,
            method="POST",
        )

    def configure_table(
        self,
        table_id,
        *,
        check_cadence_type=None,
        definition=None,
        time_column_type=None,
        notify_after=None,
        time_columns=None,
        fresh_after=None,
        interval_skip_expr=None,
        notification_channel_id=None,
        slack_users=None,
        check_cadence_run_at_duration=None,
    ):
        time_columns = [] if time_columns is None else time_columns
        slack_users = {} if slack_users is None else slack_users

        return self._api_call(
            "configure_table",
            table_id=table_id,
            method="POST",
            check_cadence_type=check_cadence_type,
            definition=definition,
            time_column_type=time_column_type,
            notify_after=notify_after,
            notification_channel_id=notification_channel_id,
            time_columns=time_columns,
            fresh_after=fresh_after,
            interval_skip_expr=interval_skip_expr,
            slack_users=slack_users,
            check_cadence_run_at_duration=check_cadence_run_at_duration,
        )


class CLI(Client):
    output_style = "text"

    def _warehouse_ids(self, warehouse_id=None):
        warehouse_ids = {int(wh["id"]) for wh in self.list_warehouses()["warehouses"]}
        if warehouse_id:
            warehouse_id = int(warehouse_id)
            if warehouse_id not in warehouse_ids:
                raise Exception(f"Warehouse with ID {warehouse_id} not found")
            return {warehouse_id}
        return warehouse_ids

    def _table_ids(self, warehouse_id, table_id=None):
        table_ids = {
            int(t["table"]["id"])
            for t in self.configured_tables(warehouse_id=warehouse_id)
        }
        if table_id:
            table_id = int(table_id)
            if table_id not in table_ids:
                raise Exception(
                    f"Table ID {table_id} not found in warehouse with ID {warehouse_id}"
                )
            return {table_id}
        return table_ids

    def _retrieve_checks_for_table(self, table_id):
        result = self.get_checks_for_table(table_id=table_id)
        checks = []
        for raw_check in [c for c in result["checks"] if c["check_static_id"]]:
            checks.append(
                {
                    "params": (
                        raw_check["config"]["params"]
                        | {
                            "check_static_id": raw_check["check_static_id"],
                            "notification_channel": raw_check[
                                "additional_notification_channel_id"
                            ],
                        }
                    ),
                    "check": raw_check["config"]["check"],
                }
            )
        return checks

    def save_checks(self, filename, warehouse_id=None, table_id=None):
        self.output_style = "json"
        component = "checks"
        if table_id and not warehouse_id:
            raise Exception("--warehouse_id is required when --table_id is provided")
        encoder = Encoder(filename)
        warehouse_ids = self._warehouse_ids(warehouse_id=warehouse_id)
        checks_by_warehouse_by_table = defaultdict(dict)
        checks_count = 0
        for wh_id in warehouse_ids:
            wh_id_key = f"warehouse_{wh_id}"
            table_ids = self._table_ids(warehouse_id=wh_id, table_id=table_id)
            for tbl_id in table_ids:
                tbl_id_key = f"table_{tbl_id}"
                checks = self._retrieve_checks_for_table(tbl_id)
                if checks:
                    checks_by_warehouse_by_table[wh_id_key][tbl_id_key] = checks
                    checks_count += len(checks)
                    print(
                        f"Retrieved {len(checks_by_warehouse_by_table[wh_id_key][tbl_id_key])} "
                        f"checks in warehouse {wh_id} and table {tbl_id}"
                    )
        with open(filename, "w") as out_file:
            encoder.save(checks_by_warehouse_by_table, component, out_file)
        print(f"Saved {checks_count} checks")

    def load_checks(self, filename, warehouse_id=None, table_id=None):
        self.output_style = "json"
        component = "checks"
        if table_id and not warehouse_id:
            raise Exception("--warehouse_id is required when --table_id is provided")
        encoder = Encoder(filename)
        checks_cache_by_table = defaultdict(dict)
        checks_count = 0
        with open(filename) as in_file:
            checks_by_warehouse_by_table = encoder.load(component, in_file)
            for wh_id, wh_data in checks_by_warehouse_by_table.items():
                wh_id = int(wh_id.removeprefix("warehouse_"))
                if warehouse_id and wh_id != int(warehouse_id):
                    continue
                for tbl_id, checks in wh_data.items():
                    tbl_id = int(tbl_id.removeprefix("table_"))
                    if table_id and tbl_id != int(table_id):
                        continue
                    if tbl_id not in checks_cache_by_table:
                        checks_cache_by_table[tbl_id] = {
                            check["params"]["check_static_id"]: check
                            for check in self._retrieve_checks_for_table(
                                table_id=tbl_id
                            )
                        }
                    for check in checks:
                        static_id = check["params"]["check_static_id"]
                        if checks_cache_by_table[tbl_id][static_id] == check:
                            # No changes
                            continue
                        print(
                            f"Loading updated check {static_id} "
                            f"in warehouse {wh_id} and table {tbl_id}"
                        )
                        self.create_check(tbl_id, check["check"], **check["params"])
                        checks_count += 1
        print(
            f"Loaded {checks_count} updated checks"
            if checks_count
            else "No checks to update"
        )


def main():
    fire.Fire(CLI, name="anomalo")


if __name__ == "__main__":
    main()
