// Lab: Crypto Hash Functions in Java 

// This lab uses JCA to make a simple cryptographer 
// JCA stands for Java Cryptography Architecture

import java.security.*;

public class main {

  public static void main(String[] args) {

    // Create an instance of the MessageDigest class
    MessageDigest md;

    try {
      md = MessageDigest.getInstance("SHA-256");

      // Create an array of message bytes for input
      String input = "Hello, World!";

      // use the update method of MessageDigest to process the data
      md.update(input.getBytes());

      // Calculate the hash value
      byte[] hashBytes = md.digest();

      System.out.println("hash value: " + hashBytes);

    } catch (NoSuchAlgorithmException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }


  }
}
