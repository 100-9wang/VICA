package chap_04;

public class _04_for {
    public static void main(String[] args) {
        // 반복문 For

        // 반복문 규칙 For
//        for (선언;조건;증감) {
//     선언을 조건을 충족할때까지 증감시킴
//        }

        for (int i = 0; i < 10 ; i++) {
            //System.out.println("어서오세요, 미니입니다" + i);
            System.out.println("환영합니다, 민희입니다" + i);
        }

        // 짝수만 출력
        for (int i = 0; i < 10; i += 2) {
            System.out.println(i);
        }

        System.out.println();

        // 홀수만 출력
        for (int j = 1; j < 10; j += 2) {
            System.out.println(j);
        }

        System.out.println();

        // 거꾸로 출력
        for (int a = 5; a > 0; a--){
            System.out.println(a);
        }
        System.out.println();

        // 가우스 수학
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        System.out.println("1 to 10 의 총합은 " + sum + "입니다");
    }
}
