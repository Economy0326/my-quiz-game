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
        return [
            Quiz(
                "git의 버전 확인 명령어는?",
                ["git status", "git log", "git show", "git version"],
                4
            ),
            Quiz(
                "Python 파일의 기본 확장자는?",
                [".java", ".py", ".js", ".cpp"],
                2
            ),
            Quiz(
                "리스트를 만들 때 사용하는 기호는?",
                ["{}", "()", "[]", "<>"],
                3
            ),
            Quiz(
                "파이썬에서 허용되지 않은 식별자는?",
                ["my_variable", "2nd_variable", "_private_var", "class"],
                2
            ),
            Quiz(
                "반복문 키워드가 아닌 것은?",
                ["for", "while", "loop", "break"],
                3
            ),
        ]


class QuizGame:
    def __init__(self):
        self.quizzes = Quiz.get_default_quizzes()
        self.best_score = 0

    # 메뉴 출력 기능
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

    # 메인 루프
    def run(self):
        while True:
            self.show_menu()
            choice = input("선택: ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                print("퀴즈 목록 기능은 아직 준비 중입니다.")
            elif choice == "4":
                print("점수 확인 기능은 아직 준비 중입니다.")
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
    
    # 퀴즈 풀기 기능
    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n 퀴즈 시작 (총 {total}문제)")

        for index, quiz in enumerate(self.quizzes, start=1):
            print("\n" + "-" * 40)
            print(f"[문제 {index}]")
            quiz.display()

            while True:
                answer = input("정답 입력 (1-4): ").strip()

                if answer == "":
                    print("빈 입력입니다. 다시 입력하세요.")
                    continue

                try:
                    answer = int(answer)
                except ValueError:
                    print("숫자를 입력하세요.")
                    continue

                if answer < 1 or answer > 4:
                    print("1-4 사이의 숫자를 입력하세요.")
                    continue

                break

            if quiz.is_correct(answer):
                print("정답입니다")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n" + "=" * 40)
        print(f"결과: {total}문제 중 {score}문제 정답")
        print("=" * 40)

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다")

    # 퀴즈 추가 기능
    def add_quiz(self):
        print("\n 새로운 퀴즈를 추가합니다.")

        question = input("문제를 입력하세요: ").strip()
        if not question:
            print("문제는 비워둘 수 없습니다.")
            return

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            if not choice:
                print("선택지는 비워둘 수 없습니다.")
                return
            choices.append(choice)

        while True:
            answer = input("정답 번호 (1-4): ").strip()

            if answer == "":
                print("빈 입력입니다. 다시 입력하세요.")
                continue

            try:
                answer = int(answer)
            except ValueError:
                print("숫자를 입력하세요.")
                continue

            if answer < 1 or answer > 4:
                print("1-4 사이의 숫자를 입력하세요.")
                continue

            break

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        print("퀴즈가 추가되었습니다!")

if __name__ == "__main__":
    game = QuizGame()
    game.run()