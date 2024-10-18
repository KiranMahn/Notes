import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

public class main {

    public static String hexRepresentationDigest(byte[] d) {
        StringBuilder sb = new StringBuilder();
        for (byte b : d) {
            sb.append(String.format("%02x", b & 0xff));
        }
        return sb.toString();
    }

    private static String generateSHA256Hash(String input) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hashBytes = digest.digest(input.getBytes());
        return hexRepresentationDigest(hashBytes);
    }

    public static void main(String[] args) {
        String filePath = "commonpasswords.txt"; 
        Map<String, String> wordHashMap = new HashMap<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String hash = generateSHA256Hash(line);
                wordHashMap.put(hash, line);
            }
        } catch (IOException | NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        // Print out the map contents (Optional)
        // System.out.println("\nWord-Hash Map:");
        // for (Map.Entry<String, String> entry : wordHashMap.entrySet()) {
        //     System.out.println(entry.getKey() + " : " + entry.getValue());
        // }

        // now go through the hashed passwords

        try (BufferedReader reader = new BufferedReader(new FileReader("hashedpasswords.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if(wordHashMap.containsKey(line)) {
                    String decodedPswd = wordHashMap.get(line);
                    System.out.println("We've cracked it! idiots! their password contained: " + decodedPswd);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
