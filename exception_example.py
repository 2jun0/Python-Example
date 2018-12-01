class NegativeInputError(Exception):

    def __str__(self):
        return "NagativeInputError"

class EmptyLineError(Exception):

    def __str__(self):
        return 'EmptyLineError'

class InputCountError(Exception):

    def __str__(self):
        return 'InputCountError'

class UnKnownOpcodeError(Exception):

    def __str__(self):
        return 'UnKnownOpcodeError'


def exception_example():
    try:
        file = open("input.txt", 'r')

        i = 1
        while True:
            line = file.readline()
            if not line:
                break
            else:
                line = line.strip()

            try:
                if line == "":
                    raise EmptyLineError()

                tokens = line.split(" ")
                if len(tokens) != 3:
                    raise InputCountError()

                a = int(tokens[1])
                b = int(tokens[2])
                if a < 0 or b < 0:
                    raise NegativeInputError()

                if tokens[0] == "ADD":
                    result = a + b
                elif tokens[0] == "SUB":
                    result = a - b
                elif tokens[0] == "MUL":
                    result = a * b
                elif tokens[0] == "DIV":
                    result = int(a / b)
                else:
                    raise UnKnownOpcodeError()

            except NegativeInputError as e:
                print('{}: 데이터에 음수가 있습니다.'.format(i))
            except ValueError as e:
                print('{}: 잘못된 피연산자가 있습니다.'.format(i))
            except InputCountError as e:
                print('{}: 피연산자의 수가 잘못되었습니다.'.format(i))
            except EmptyLineError as e:
                print('{}: 명령에 빈 줄이 있습니다.'.format(i))
            except UnKnownOpcodeError as e:
                print('{}: 알 수 없는 명령어가 있습니다.'.format(i))
            except ZeroDivisionError as e:
                print('{}: 나눗셈 연산의 피연산자로 0이 입력되었습니다.'.format(i))
            finally:
                if result:
                    print('{} : {}'.format(line,result))
                else:
                    print('{}'.format(line))
                
                i = i + 1

        file.close()
    except FileNotFoundError as e:
        print("파일을 열 수 없습니다")
        exit()
    except PermissionError as e:
        print("파일이 열려 있습니다.")
        exit()


def main():
    exception_example()


if __name__ == "__main__":
    main()
