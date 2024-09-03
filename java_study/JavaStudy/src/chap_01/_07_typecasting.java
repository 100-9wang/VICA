package chap_01;

public class _07_typecasting {
    public static void main(String[] args) {
        // 형변환 typecasting 이란?
        // 정수형 -> 실수형
        // 실수형 -> 정수형

        //int score = 93 + 98.8;

        //int -> (float, double)
        int score = 93;
        System.out.println(score); // 93
        System.out.println((float) score);
        System.out.println((double) score);

        //(float, double) -> int
        float score_f = 93.5F;
        double score_d = 98.8;
        System.out.println((int)score_f);
        System.out.println((int)score_d);

        //정수 + 실수 연산
        score = 93 + (int) 98.8;
        System.out.println(score);


        score_d = (double) 93 + 98.8;
        System.out.println(score_d);

        //변수에 형변환된 데이터 집어넣기
        double convertedScoreDouble = score;
        // int -> long -> float -> double (자동 형변환) 작은 범위에서 큰 범위로

        int convertedScoreInt = (int)score_d; // 191.8 -> 191
        // double -> float -> long -> int (수동 형변환) 큰 범위에서 작은 범위로

        // 숫자 -> 문자
        String s1 = String.valueOf(93);
        s1 = Integer.toString(93);
        System.out.println(s1);

        String s2 = String.valueOf(98.8);
        s2 = Double.toString(98.8);
        System.out.println(s2);

        // 문자 -> 숫자
        int i = Integer.parseInt("93");
        System.out.println(i);

        double d = Double.parseDouble("98.8");
        System.out.println(d);

//        int error = Integer.parseInt("자바");
//        System.out.println(error);
    }
}
