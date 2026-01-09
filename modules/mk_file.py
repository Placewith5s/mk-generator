from typing import Literal

Common_Mk_Name = Literal["makefile"]
Common_File = Literal["main.cpp"] | Literal["main.py"] | Literal["main.ts"]

new_line_n_tab: str = "\n\t"
next_n_skip_line: str = "\n\n"
new_line: str = "\n"
tab: str = "\t"
cplusplus_source, py_source, ts_source = "source=g++", "source=python3", "source=npx tsc"

upd_cplusplus: str = f"update:{new_line_n_tab}@g++ $(target) -o $(program)"
run_cplusplus: str = f"run: $(target){new_line_n_tab}@./$(program)"
run_python3: str = f"run: $(target){new_line_n_tab}@$(source) $(target)"
run_ts: str = f"$(js_file): $(target){new_line_n_tab}@$(source){new_line}update:{new_line_n_tab}@$(target)"


# This function is used by the module
# file_name: str - The file name for the makefile
def new_mk(file_name: str):
    return open(f"{file_name}.mk", "w")

def handle_new_mk(mk_name: str | None):
    if mk_name:
        file = new_mk(mk_name)
        return file
    else:
        file = new_mk("makefile")
        return file

# Creates a new makefile based on the supported choices: C++, Python, and TypeScript
# mk_name: str | None - Defaults to "makefile", if "None" is given
def create_write_mk(mk_name: Common_Mk_Name | str, target_file_name: Common_File | str) -> None:
    file = handle_new_mk(mk_name)

    cpp_choice: bool = target_file_name.endswith(".cpp")
    py_choice: bool = target_file_name.endswith(".py")
    ts_choice: bool = target_file_name.endswith(".ts")

    if cpp_choice:
        program: str = target_file_name.replace(".cpp", "")
        cplus_plus_code: str = f"{cplusplus_source}{new_line}target={target_file_name}{new_line}program={program}{next_n_skip_line}{upd_cplusplus}{next_n_skip_line}{run_cplusplus}"
        file.write(cplus_plus_code)
    elif py_choice:
        python_mk_code: str = f"{py_source}{new_line}target={target_file_name}{next_n_skip_line}{run_python3}"
        file.write(python_mk_code)
    elif ts_choice:
        js_file: str = target_file_name.replace(".ts", ".js")
        ts_mk_code: str = f"{ts_source}{new_line}target={target_file_name}{new_line}js_file={js_file}{next_n_skip_line}{run_ts}"
        file.write(ts_mk_code)

    file.close()