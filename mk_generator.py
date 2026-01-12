__version__: str = "1.0.1"

from typing import Literal

Common_Mk_Name = Literal["makefile"]
Common_File = Literal["main.cpp"] | Literal["main.py"] | Literal["main.ts"]

__new_line_n_tab: str = "\n\t"
__next_n_skip_line: str = "\n\n"
__new_line: str = "\n"
__cplusplus_source, __py_source, __ts_source = "source=g++", "source=python3", "source=npx tsc"

__upd_cplusplus: str = f"update:{__new_line_n_tab}@g++ $(target) -o $(program)"
__run_cplusplus: str = f"run: $(target){__new_line_n_tab}@./$(program)"
__run_python3: str = f"run: $(target){__new_line_n_tab}@$(source) $(target)"
__run_ts: str = f"$(js_file): $(target){__new_line_n_tab}@$(source){__new_line}update:{__new_line_n_tab}@$(target)"


# This function is used by the module
# file_name: str - The file name for the makefile
def __new_mk(file_name: str):
    return open(f"{file_name}.mk", "w")

def __handle_new_mk(mk_name: str | None):
    if mk_name:
        file = __new_mk(mk_name)
        return file
    else:
        file = __new_mk("makefile")
        return file

# Creates a new makefile based on the supported choices: C++, Python, and TypeScript
# mk_name: str | None - Defaults to "makefile", if "None" is given
def create_write_mk(mk_name: Common_Mk_Name | str, target_file_name: Common_File | str) -> None:
    file = __handle_new_mk(mk_name)

    cpp_choice: bool = target_file_name.endswith(".cpp")
    py_choice: bool = target_file_name.endswith(".py")
    ts_choice: bool = target_file_name.endswith(".ts")

    if cpp_choice:
        program: str = target_file_name.replace(".cpp", "")
        cplus_plus_code: str = f"{__cplusplus_source}{__new_line}target={target_file_name}{__new_line}program={program}{__next_n_skip_line}{__upd_cplusplus}{__next_n_skip_line}{__run_cplusplus}"
        file.write(cplus_plus_code)
    elif py_choice:
        python_mk_code: str = f"{__py_source}{__new_line}target={target_file_name}{__next_n_skip_line}{__run_python3}"
        file.write(python_mk_code)
    elif ts_choice:
        js_file: str = target_file_name.replace(".ts", ".js")
        ts_mk_code: str = f"{__ts_source}{__new_line}target={target_file_name}{__new_line}js_file={js_file}{__next_n_skip_line}{__run_ts}"
        file.write(ts_mk_code)

    file.close()