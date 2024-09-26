package chap_04;

public class _02_elseIf {
    public static void main(String[] args) {
        // 조건문 elseif
        // 한라봉 에이드가 있으면 + 1
        // 또는 망고 주스가 있으면 + 1
        // 또는 아이스 아메리카노 + 1
        boolean 한라봉에이드 = true;
        boolean 망고주스 = true;

        if (한라봉에이드) {
            System.out.println("한라봉 에이드 + 1");
        } else if (망고주스) {
            System.out.println("망고주스 + 1");
        } else {
            System.out.println("아이스 아메리카노 + 1");
        }
        System.out.println("커피 주문 완료 #1");

        // else if 는 여러번 사용 가능
        한라봉에이드 = false;
        망고주스 = false;
        boolean 오렌지주스 = true;
        if (한라봉에이드) {
            System.out.println("한라봉 에이드 + 1");
        } else if (망고주스) {
            System.out.println("망고주스 + 1");
        } else if (오렌지주스) {
            System.out.println("오렌지주스 + 1");
        } else {
            System.out.println("아이스 아메리카노 + 1");
        }
        System.out.println("커피 주문 완료 #2");

    }
}

