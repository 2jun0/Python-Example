class NegativeInputError(Exception):
# 음수 입력 예외
    def __str__(self):
        return "NagativeInputError"

class EmptyLineError(Exception):
# 공백 명령줄 예외
    def __str__(self):
        return 'EmptyLineError'

class InputCountError(Exception):
# 피연산자 개수 예외
    def __str__(self):
        return 'InputCountError'

class UnKnownOpcodeError(Exception):
# 미정의 명령어 예외
    def __str__(self):
        return 'UnKnownOpcodeError'


def exception_example():
    # input.txt를 읽어서 명령어를 실행하는 함수이다.
    try:
        # input.txt를 읽기모드로 연다.
        file = open("input.txt", 'r')

        # i는 줄 수 카운팅하는 변수
        # 시작 줄은 1
        i = 1

        while True:

            # 결과값 초기화 : 명령어가 제대로 수행됬는지를 식별하기 위해 사용
            result = None

            # 파일에서 한 줄 읽는다.
            line = file.readline()

            # 더 이상 읽을 내용이 없는 경우
            if not line:
                # while문 벗어남(읽기 종료)
                break
            else:
                # 아닌경우 개행문자 제거 (파이썬은 readline 함수를 호출하면 개행문자도 같이 저장한다.)
                line = line.strip()

            try:
                # 읽어들인 한 줄이 공백인 경우
                if line == "":
                    # 공백 예외 발생
                    raise EmptyLineError()

                # " "로 쪼갠다
                # tokens[0] = 명령어
                # tokens[1] = 첫번째 피연산자
                # tokens[2] = 두번째 피연산자
                tokens = line.split(" ")
                if len(tokens) != 3:
                    # 입력개수가 3개가 아니라면(피연산자는 2개, 명령어 포함 3개)
                    # 입력 개수 예외 발생
                    raise InputCountError()

                # string인 tokens[1], tokens[2]를 int형으로 바꾼다.
                a = int(tokens[1])
                b = int(tokens[2])

                # 피연산자 중 하나라도 음수이면
                if a < 0 or b < 0:
                    # 음수 입력 예외 발생
                    raise NegativeInputError()

                # tokens[0](명령어)를 분석한다.
                # 결과값은 result에 저장되며
                if tokens[0] == "ADD":
                    # 더하기 명령어
                    result = a + b
                elif tokens[0] == "SUB":
                    # 빼기 명령어
                    result = a - b
                elif tokens[0] == "MUL":
                    # 곱하기 명령어
                    result = a * b
                elif tokens[0] == "DIV":
                    # 나누기 명령어
                    result = int(a / b)
                else:
                    # 정의되어 있지 않은 명령어 에러 발생
                    raise UnKnownOpcodeError()

            # 예외처리
            except NegativeInputError as e:
                # 입력이 음수 일 때
                print('{}: 데이터에 음수가 있습니다.'.format(i))
            except ValueError as e:
                # int(string) 할때의 string이 정수가 아닌경우
                # (기본으로 제공되는 예외)
                print('{}: 잘못된 피연산자가 있습니다.'.format(i))
            except InputCountError as e:
                # 입력한 피연산자의 수가 2개가 아닌경우
                print('{}: 피연산자의 수가 잘못되었습니다.'.format(i))
            except EmptyLineError as e:
                # 명령어에 빈 줄이 있는 경우
                print('{}: 명령에 빈 줄이 있습니다.'.format(i))
            except UnKnownOpcodeError as e:
                # 명령어가 정의되어 있지 않은 경우
                print('{}: 알 수 없는 명령어가 있습니다.'.format(i))
            except ZeroDivisionError as e:
                # 나눗셈 연산시 0으로 나눌 때
                # (기본으로 제공되는 예외)
                print('{}: 나눗셈 연산의 피연산자로 0이 입력되었습니다.'.format(i))
            finally:
                # 계산에 성공하면 결과값을 보여주고 아니면 결과값을 빼고 출력한다.
                if result:
                    print('{} : {}'.format(line,result))
                else:
                    print('{}'.format(line))

                # 줄 수 넘버링
                i = i + 1

        file.close()
    except FileNotFoundError as e:
        # 파일이 없는 경우
        # (기본으로 제공되는 예외)
        print("파일을 열 수 없습니다")
        # 프로그램 종료
        exit()
    except IOError as e:
        # 입출력 오류 ( 파일이 열려있는 지 확인 할 수 없기 때문에 입출력 에러로 대체 )
        # (기본으로 제공되는 예외)
        print("파일이 열려 있습니다.")
        # 프로그램 종료
        exit()

# main 함수 (이 프로그램의 시작 함수)
def main():
    exception_example()

# 처음 실행될 때 main함수 호출
if __name__ == "__main__":
    main()
