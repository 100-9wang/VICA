package chap_02;

import java.util.Scanner;

public class _quiz_02 {
    public static void main(String[] args) {
        //어린이 키에 따른 놀이 기구 탑승 가능 여부를 확인하는 프로그램을 작성하시오.

        // 조건
        // 1. 키가 120cm 이상인 경우에만 탑승 가능
        // 2. 삼항 연산자 이용

        // 계산식
        System.out.println("탑승자의 키를 입력해주세요");
        Scanner s = new Scanner(System.in);
        int high = s.nextInt();

        String result = (high >= 120) ? ("탑승 가능합니다") : ("탑승 불가능합니다");
        System.out.println("어린이의 키가 " + high + "cm 이므로 " + result);
    }
}
