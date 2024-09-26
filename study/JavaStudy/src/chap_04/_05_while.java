package chap_04;

public class _05_while {
    public static void main(String[] args) {
        // 반복문 while
        int distance = 25; // 전체거리 25m
        int move = 0;

        while (move <= distance) { // 현재 이동 거리가 전체 거리보다 작다는 조건이 참인 동안 반복동작
            System.out.println("발차기를 계속 합니다.");
            System.out.println("현재 이동 거리는 " + move);
            move += 1;
        }
        System.out.println("도착하였습니다.");


        // 무한 루프
        // 무한 루프에 빠지지 않게 빠져나오는 동작을 설정해줘야 함.
        move = 0;
        while (move <= distance) {
            System.out.println("발차기를 계속 합니다.");
            System.out.println("현재 이동 거리는 " + move);
        }
        System.out.println("도착하였습니다.");
    }
}
