package chap_03;

import java.util.Locale;

public class _01_string1 {
    public static void main(String[] args) {
        String s = "I like Java and Python and C";
        System.out.println(s);

        // 문자열의 길이 ( length )
        System.out.println(s.length()); // 28

        // 대소문자 변환 ( upper / lower )
        System.out.println(s.toUpperCase());
        System.out.println(s.toLowerCase());

        // 포함 관계 ( contains / indexOf / startsWith / endsWith)
        System.out.println(s.contains("Java")); // 대소문자 구분함
        System.out.println(s.contains("C#"));
        System.out.println(s.indexOf("Java")); // 위치 정보
        System.out.println(s.indexOf("C#")); // 비포함시 -1 반환
        System.out.println(s.indexOf("and")); // 처음 일치
        System.out.println(s.lastIndexOf("and")); // 마지막 일치
        System.out.println(s.startsWith("I like")); // 이 문자열로 시작하면 true else flase
        System.out.println(s.endsWith("C"));
    }
}
