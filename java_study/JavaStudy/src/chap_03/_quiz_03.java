package chap_03;

import java.util.Scanner;

public class _quiz_03 {
    public static void main(String[] args) {
        // 주민등록번호에서 생년월일 및 성별까지만 출력하는 프로그램을 작성하시오

        // 참고
        // 주민등록번호 13자리의 숫자로 구성
        // 앞 6자리는 생년월일 정보, 뒷 7자리 중 첫 번째 숫자는 성별 정보
        // 입력 데이터는 -를 포함한 14자리의 문자열 형태

        // ex)
        // "901231 - 1234567 인 경우 901231 - 1 까지 출력

        String s1 = "011110-1234567";
        System.out.println(s1.substring(s1.indexOf("0"), s1.indexOf("2")));

        String s2 = "011110-4567891";
        System.out.println(s2.substring(0, 8));
        // 공통 숫자 제외 ( - )
        System.out.println(s2.substring(0, s2.indexOf("-") + 2));

//        // 직접 입력 받기
//        System.out.println("주민등록번호를 입력하세요");
//        Scanner s = new Scanner(System.in);
//        String id = s.next();
//        System.out.println("입력하신 주민등록 번호는 " + id.substring(0, 8) + " 입니다");
    }
}
