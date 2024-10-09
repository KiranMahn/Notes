import java.security.*;

import javax.crypto.KeyGenerator;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

public class main {
    public static void main(String[] args) {
        try {

            KeyPairGenerator keyGen = KeyPairGenerator.getInstance("DSA");

            SecureRandom prng = SecureRandom.getInstance("SHA1PRNG");

            int keySize = 1024;

            keyGen.initialize(keySize,prng);

            KeyPair kp = keyGen.generateKeyPair();

            PublicKey puk = kp.getPublic();
            PrivateKey prk = kp.getPrivate();

            Signature sig = Signature.getInstance("DSA");

            sig.initSign(prk);

            String filePath = "test.txt"; // Change this to your file's path
            byte[] byteArray;
            try {
                byteArray = Files.readAllBytes(Paths.get(filePath));
                System.out.println("File content as byte array: " + byteArray.length + " bytes");
                sig.update(byteArray);

                
            } catch (IOException e) {
                e.printStackTrace();
            }

            sig.sign();

            System.out.println("sig: " + sig.toString());

            
            

        } catch (NoSuchAlgorithmException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (InvalidKeyException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (SignatureException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }
}
