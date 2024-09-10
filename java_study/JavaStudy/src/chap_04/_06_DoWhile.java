package chap_04;

public class _06_DoWhile {
    public static void main(String[] args) {
        // 반복문 while
        int distance = 25;
        int move = 0;
        int height = 2;

        while (move + height < distance) {
            System.out.println("발차기를 계속 합니다.");
            System.out.println("현재 이동 거리는 " + move);
            move += 3;
        }
        System.out.println("도착하였습니다.");

        System.out.println(" --- 반복문 #1 --- ");

        // 반복문 DoWhile
        distance = 25;
        move = 0;
        height = 25;
        do {
            System.out.println("발차기를 계속 합니다.");
            System.out.println("현재 이동 거리 : " + move);
            move += 3;
        } while (move + height < distance);
        System.out.println("도착했습니다");
    }
}
