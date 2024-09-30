public class main {
    public static void main (String[] args) {

        String alphabet = "abcdefghijklmnopqrstuvwxyz";

        String key = "key";

        char[] keyArray = key.toCharArray();

        // String phrase = "hello";
        String phrase = "I shall call him squishy and he shall be mine and he shall be my squishy";
        
        phrase = phrase.toLowerCase();

        char[] ciphertext = phrase.toCharArray();

        int j = 0;

        for(int i = 0; i < phrase.length(); i++) {
            if(ciphertext[i] != ' ') {
                // System.out.println("adding " + ciphertext[i] + " (" + alphabet.indexOf(ciphertext[j]) + ") + " +  alphabet.indexOf(keyArray[j]));

                int total = alphabet.indexOf(ciphertext[i]) + alphabet.indexOf(keyArray[j]);
    
                if(total >= 26) {
                    total = total - 26;
                }
    
                ciphertext[i] = alphabet.charAt(total);
    
                // System.out.println("new value: " + ciphertext[i]);
    
                if(j == key.length() - 1) {
                    j = 0;
                } else {
                    j++;
                }
            }
        }

        String result = new String(ciphertext);

        result = result.replace(" ", "");

        result = result.toUpperCase();

        System.out.println(result);

        String answer = "SWFKPJMEJVLGWWOEMQRCYXHFOWFKPJLIKSRCKRBRIQREJVFCWCQAYGCLW";

        if(result.equals(answer)) {
            System.out.println("true");
        }

    }
}