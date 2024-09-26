package chap_04;

import java.util.Scanner;

public class _03_switchCase {
    public static void main(String[] args) {
        // Switch Case
        // < 석차에 따른 장학금 지급 >
        // 1등 : 전액 장학금
        // 2등 : 반액 장학금
        // 3등 : 반액 장학금
        // 그 외 : 장학금 대상 제외

        // if else 문 이용 (여러 조건 또는 범위에 대한 조건)
        int rank1 = 4;
        if (rank1 == 1) {
            System.out.println("전액 장학금 대상입니다.");
        } else if(rank1 == 2 || rank1 == 3) {
            System.out.println("반액 장학금 대상입니다.");
        } else {
            System.out.println("장학금 대상이 아닙니다.");
        }
        System.out.println("장학금 대상 조회  #1");

        // Switch Case 문 이용 (명확한 케이스가 있는 경우)
        System.out.println("등 수를 입력하세요.");
        Scanner s = new Scanner(System.in);
        int rank = s.nextInt();

        switch (rank){
            case 1 :
                System.out.println("전액 장학금 대상입니다.");
                break;
            case 2 :
                System.out.println("반액 장학금 대상입니다.");
                break;
            case 3 :
                System.out.println("반액 장학금 대상입니다.");
                break;
            default :
                System.out.println("장학금 대상이 아닙니다.");
        }
        System.out.println("장학금 대상 조회 #2");

        System.out.println("등 수를 입력하세요.");
        Scanner s1 = new Scanner(System.in);
        int rank2 = s.nextInt();

        // case 2와 3이 같은 동작 값일 때 통합
        switch (rank2){
            case 1 :
                System.out.println("전액 장학금 대상입니다.");
                break;
            case 2 :
            case 3 :
                System.out.println("반액 장학금 대상입니다.");
                break;
            default :
                System.out.println("장학금 대상이 아닙니다.");
        }
        System.out.println("장학금 대상 조회 #3");

        // 중고 상품의 등급에 따른 가격을 책정 ( 1급 : 최상, 4급 : 최하 )
        System.out.println("상품의 등급을 입력해주세요.");
        Scanner g = new Scanner(System.in);
        int grade = g.nextInt();
        int price = 8000; // 기본 가격

        switch(grade) {
            case 1:
                price += 1000; //price = price + 1000;
            case 2:
                price += 1000;
            case 3:
                price += 1000;
                break;
        }
        System.out.println(grade + "등급 제품의 가격 : " + price + "원");
        System.out.println("중고 상품 등급별 가격 책정 #1");

        }
    }
