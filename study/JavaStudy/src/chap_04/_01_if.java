package chap_04;

public class _01_if {
    public static void main(String[] args) {
        int hour = 17; // 오전 10시
//        // 조건문 if
//        if (hour < 14) {
//            System.out.println("아이스 아메리카노 + 1");
//            System.out.println("샷 추가");
//            System.out.println("커피 주문 완료");
//        } else {
//            System.out.println("페퍼민트 티 + 1");
//            System.out.println("얼음 많이");
//            System.out.println("페퍼민트 티 주문 완료");
//        }

        // 오후 2시 이전 and 모닝 커피를 마시지 않은 경우 ?
        hour = 18;
        boolean morningCoffe = true;
        if (hour < 14 && !morningCoffe) {
            System.out.println("아이스 아메리카노 + 1");
            System.out.println("샷 추가");
            System.out.println("커피 주문 완료");
        } else {
            System.out.println("커피 하루 권장량이 넘었습니다");
            System.out.println("과도한 카페인 섭취는 수면장애를 유발할 수 있습니다");
        }

        // 오후 2시 이후이거나 모닝 커피를 마신 경우 ?
        hour = 15;
        morningCoffe = true;
        if (hour >= 14 || morningCoffe) {
            System.out.println("아이스 아메리카노 (디카페인) + 1");
        }
    }
}
