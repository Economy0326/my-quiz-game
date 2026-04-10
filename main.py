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


class QuizGame:
    def __init__(self):
        self.quizzes = []
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