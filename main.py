class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 퀴즈 문제와 선택지를 출력하는 기능
    def display(self):
        print(self.question)
        # enumerate: 리스트의 각 요소에 대해 인덱스와 함께 반복할 수 있게 해주는 함수
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    # 정답 확인 기능
    def is_correct(self, user_answer):
        return user_answer == self.answer
    
    def get_default_quizzes():
      # 0인덱스로 사용 예정
      return [
          Quiz(
              "git의 버전 확인 명령어는?",
              ["git status", "git log", "git show", "git version"],
              3
          ),
          Quiz(
              "Python 파일의 기본 확장자는?",
              [".java", ".py", ".js", ".cpp"],
              1
          ),
          Quiz(
              "리스트를 만들 때 사용하는 기호는?",
              ["{}", "()", "[]", "<>"],
              2
          ),
          Quiz(
              "파이썬에서 허용되지 않은 식별자는?",
              ["my_variable", "2nd_variable", "_private_var", "class"],
              1
          ),
          Quiz(
              "반복문 키워드가 아닌 것은?",
              ["for", "while", "loop", "break"],
              2
          ),
      ]


class QuizGame:
    def __init__(self):
      self.quizzes = get_default_quizzes()
      self.best_score = 0

    def show_menu(self):
        print("=" * 40)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def run(self):
        while True:
            self.show_menu()
            choice = input("선택: ").strip()

            if choice == "1":
                print("퀴즈 풀기 기능은 아직 준비 중입니다.")
            elif choice == "2":
                print("퀴즈 추가 기능은 아직 준비 중입니다.")
            elif choice == "3":
                print("퀴즈 목록 기능은 아직 준비 중입니다.")
            elif choice == "4":
                print("점수 확인 기능은 아직 준비 중입니다.")
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()