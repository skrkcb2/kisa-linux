# -*- coding: utf-8 -*-
import inspect
import dic_linux_secure2 as dls
import subprocess
import re

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def compare_check(res):

    print("============================================" + res + "============================================")

    path = dls.check[res]['path']

    if path[0] == 'pass':
        print(YELLOW +  "점검 미실시 | " + res + " | 전 항목과 겹칩니다." + RESET)
        return

    if path[0] == 'pass_2':
        print(YELLOW + "점검 미실시 | " + res + " | 전 항목과 겹칩니다." + RESET)
        return

    check_point = dls.check[res]['check_point']

    check_plag = 0

    if "cm_line" in dls.check[res]:
        sub_line = dls.check[res]['cm_line']
        for l in sub_line:
            print(YELLOW + l  + RESET)
        check_plag += 1

    else:
        sub_line = dls.check[res]['check_point']
        for l in sub_line:
            print(YELLOW + l + RESET)

        print(GREEN + "\n점검 명령어 | " + path[0] + "\n" +RESET)
        print(GREEN + "점검 완료 | 해당 케이스는 민감 혹은 아이체크가 필요"+ "\n" + RESET)
        result = subprocess.run(path[0], stdout=subprocess.PIPE, shell=True)
        res_in = result.stdout.decode('utf-8').strip() or "출력 결과가 없습니다."
        print(res_in + RESET)


    try:
        if check_plag == 1:
            print('\n' + GREEN + "점검 명령어 | " + path[0] + '\n' + RESET)

            command = path[0]
            result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
            result = result.stdout
            result = result.decode('utf-8').split('\n')

            if res.replace("'", "") == "U_6_FD_OWN":
                check_point.clear()
                check_point = [r for r in result if r != ""]
                result.pop(1)
            else:
                if len(result) == 1:
                    pass
                else:
                    result.pop()

            for index, r_res in enumerate(result):
                if all(str(sublist) in r_res for sublist in check_point):
                    if check_plag == 1:
                        print(GREEN + (r_res if r_res else "result: 출력 결과가 없습니다. \n") + RESET)
                    else:
                        print("점검 실패")

                else:
                    if check_plag == 1:
                        print(r_res + RESET)
                    else:
                        print("점검 실패")
        else:
            pass

    except subprocess.CalledProcessError as e:
        print(RED + e + RESET)

def execute_command(res):
    print("============================================" + res + "============================================")
    check_point = dls.check[res]['check_point']

    input_line = dls.check[res]['path']
    ex_line = dls.check[res]['ex_line']
    print(GREEN + "점검 완료 | 해당 케이스는 민감 혹은 아이체크가 필요 \n" + RESET)

    for i in ex_line:
        print (YELLOW + i + RESET)
    try:
        for index2, ck_cmd in enumerate(input_line):
            print(GREEN + "점검 명령어 | " + ck_cmd + RESET)
            if check_point[0] == '':
                result = subprocess.run(ck_cmd, stdout=subprocess.PIPE, shell=True)
                rres = result.stdout.decode('utf-8').strip() or "출력 결과가 없습니다."
                print(rres)
                print('\n')
            else:
                result = subprocess.run(ck_cmd, stdout=subprocess.PIPE, shell=True)
                rres = result.stdout.decode('utf-8').strip() or "출력 결과가 없습니다."
                rres = rres.split('\n')
                for row in rres:
                    if check_point[0] in row and not '#' in row:
                        print(GREEN + row + RESET)
                    else:
                        print(row + RESET)
                print('\n')

    except Exception as e:
        print(e)


def main():
    check_keys = list(dls.check.keys())
    index = 0

    while index < len(check_keys):
        header = check_keys[index]

        if "cm_line" in dls.check[header] or "just_line" in dls.check[header]:
            compare_check(header)
        else:
            execute_command(header)

        index += 1  # 다음 키로 이동
        input("\n다음 항목을 실행하려면 엔터를 누르세요...\n")

    print("모든 항목을 실행했습니다.")



if __name__ == "__main__":
    main()
