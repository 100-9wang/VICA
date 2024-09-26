package chap_01;

public class _quiz_01 {
    public static void main(String[] args) {
        //버스 도착 정보를 출력하는 프로그램을 작성하시오
        //각 정보는 적절한 자료형의 변수에 정의합니다.

        //정보 :
        // 버스 번호는 "1234", "상암08"과 같은 형태
        String busNo = "1234";
        System.out.println(busNo + "번 버스");

        // 남은 시간은 분 단위 (ex: 3분, 5분)
        int minute = 5;
        System.out.println("약 " + minute + "분 후 도착" );

        // 남은 거리는 km단위 (ex:1.5km, 0.8km)
        float reDistance = 0.8f;
        System.out.println("남은 거리 " + reDistance + "km");


        String busNum = "상암08";
        System.out.printf(busNum + "번 버스\n");

        int min = 3;
        System.out.println("약 " + min + "분 후 도착");

        float distance = 1.2f;
        System.out.println("남은 거리 " + distance + "km");

    }
}
