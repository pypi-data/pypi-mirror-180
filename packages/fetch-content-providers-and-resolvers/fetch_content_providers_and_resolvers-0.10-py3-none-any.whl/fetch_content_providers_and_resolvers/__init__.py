import os
import re
import subprocess
from typing import Union

from a_pandas_ex_adb_to_df import pd_add_adb_to_df
from a_pandas_ex_plode_tool import pd_add_explode_tools
from a_pandas_ex_adb_to_df import execute_multicommands_adb_shell

pd_add_adb_to_df()
from PyRipGrep import RePatterns
from list_all_files_recursively import get_folder_file_complete_path
from flatten_everything import flatten_everything
from cprinter import TC

pd_add_explode_tools()
import pandas as pd


def connect_to_adb(adb_path, deviceserial):
    _ = subprocess.run(f"{adb_path} start-server", capture_output=True, shell=False)
    _ = subprocess.run(
        f"{adb_path} connect {deviceserial}", capture_output=True, shell=False
    )


def isroot(
    adb_path, deviceserial, exit_keys="ctrl+x", print_output=False, timeout=None
):
    # from https://wuseman.se/
    roa = execute_multicommands_adb_shell(
        adb_path,
        deviceserial,
        subcommands=[
            f"""which su -- &> /dev/null
    if [[ $? = "0" ]]; then
        echo "True"
    else
        echo "False"
    fi"""
        ],
        exit_keys=exit_keys,
        print_output=print_output,
        timeout=timeout,
    )
    isrooted = False
    if roa[0].decode("utf-8", "ignore").strip() == "True":
        isrooted = True

    return isrooted


class ContentProviderResolverFetcher:
    def __init__(
        self,
        adb_path: str,
        deviceserial: str,
        folder="data/",
        folder_for_temp_files: Union[str, None] = None,
        ripgrep_path: str = "rg.exe",
    ):
        if folder_for_temp_files is None:
            folder_for_temp_files = os.getcwd()
        self.adb_path = adb_path
        self.deviceserial = deviceserial
        self.folder = folder
        self.df = pd.DataFrame()
        self.folder_for_temp_files = folder_for_temp_files
        self.ripgrep_path = ripgrep_path
        self.filelist = []
        self.allresults = []
        self.allresults_checked = pd.DataFrame()
        self.is_root = False

    def connect_to_adb(self):
        connect_to_adb(self.adb_path, self.deviceserial)
        self.is_root = isroot(
            self.adb_path,
            self.deviceserial,
            exit_keys="ctrl+x",
            print_output=False,
            timeout=None,
        )
        return self

    def get_all_files(self):
        self.df = pd.Q_adb_to_df(
            device=self.deviceserial, adb_path=self.adb_path, folder=self.folder
        )
        self.df = self.df.loc[
            (self.df.aa_size > 0) & (~self.df.aa_rights.str.contains(r"^[dl]"))
        ]
        self.df = self.df.loc[
            self.df.aa_filename.str.contains(r"\.dex$", na=False, flags=re.I)
        ]

        return self

    def pull_files(self):
        self.df.ff_pull_file_cat.apply(lambda x: x(self.folder_for_temp_files))
        self.filelist = [
            y.path for y in get_folder_file_complete_path(self.folder_for_temp_files)
        ]
        return self

    def extract_content_providers(self):
        x = self.filelist
        outputtype = "np"
        df7 = RePatterns(executeable=self.ripgrep_path).find_all_in_files_json(
            re_expression=[r"content:[^\s]{2,120}"],
            search_in=x,
            outputtype=outputtype,
            binary=True,
            ignore_case=True,
        )

        df3 = pd.Q_AnyNestedIterable_2df(df7)
        df8 = df3.loc[
            df3.aa_value.astype("string").str.contains(
                "content://", na=False, regex=False
            )
        ]
        df8 = df8.drop_duplicates(subset="aa_value")
        df8 = (
            df8.aa_value.str.extract(r"(content://[A-Za-z\d./_-]+)")
            .dropna()
            .drop_duplicates()
        )

        expres = (
            "(?:"
            + "|".join(df8[0].str.replace("content://", "").str.strip("/").to_list())
            + r")[^\s]{1,}"
        )
        df9 = RePatterns(executeable=self.ripgrep_path).find_all_in_files_json(
            re_expression=[expres],
            search_in=x,
            outputtype=outputtype,
            binary=True,
            ignore_case=True,
        )

        uiu = set(flatten_everything(df9))
        df0 = pd.DataFrame([x for x in uiu if isinstance(x, str)])

        expres2 = (
            "((?:"
            + "|".join(df8[0].str.replace("content://", "").str.strip("/").to_list())
            + r")[A-Za-z\d./_-]+)"
        )
        secondround = df0[0].str.extractall(expres2)
        secondroundlist = (
            secondround.reset_index(drop=True)
            .drop_duplicates()[0]
            .apply(lambda x: f"content://{x}")
            .to_list()
        )
        allcon = tuple(set(flatten_everything([df8[0].to_list(), secondroundlist])))
        self.allresults = allcon
        return self

    def check_results(
        self, exit_keys: str = "ctrl+x", print_output=True, timeout=None,
    ):
        resis = []
        for _ in self.allresults:
            if self.is_root:
                uu = execute_multicommands_adb_shell(
                    self.adb_path,
                    self.deviceserial,
                    [f'su -c "content query --uri {_}"'],
                    exit_keys=exit_keys,
                    print_output=print_output,
                    timeout=timeout,
                )
            else:
                uu = execute_multicommands_adb_shell(
                    self.adb_path,
                    self.deviceserial,
                    [f"content query --uri {_}"],
                    exit_keys=exit_keys,
                    print_output=print_output,
                    timeout=timeout,
                )

            if print_output:
                if uu:

                    print(TC(f"{_}").fg_green.bg_black)
                    print(uu)
                else:
                    print(TC(f"{_}").fg_yellow.bg_black)
            try:
                resis.append((_, b"".join(uu).decode("utf-8", "ignore")))
            except Exception as fe:
                print(fe)
                resis.append((_, ""))
        self.allresults_checked = pd.DataFrame(resis)
        return self

    def get_all_results(self):
        return self.allresults

    def get_all_results_checked(self):
        return self.allresults_checked.copy()
