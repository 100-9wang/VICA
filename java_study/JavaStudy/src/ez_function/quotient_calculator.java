package ez_function;

import java.util.Scanner;

public class quotient_calculator {
    public static void main(String[] args) {
        // 나눌 수 입력
        System.out.println("나누고 싶은 수를 입력하세요");
        Scanner s = new Scanner(System.in);
        int divided = s.nextInt();

        // 나누는 수 입력
        System.out.println("몇으로 나누시겠습니까 ?");
        int divisor = s.nextInt();

        // 값 초기 세팅
        int quotient = 0;
        int remainder = 0;

        // 연산 작업식
        if(divisor != 0) {
            quotient = (int) (divided / divisor); //형 변환
            remainder = divided % divisor;
            System.out.println(divided + "를" + divisor + "로 나눈 몫은" + quotient + "이고 나머지는" + remainder + "입니다");
        } else {
            System.out.println("0으로는 나눌 수 없습니다.");
        }
    }
}
