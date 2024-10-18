// import BCrypt;

public class main {
    public static void main(String[] args) {

        String password = "meow";
        String salt = BCrypt.gensalt(12);

        String securePassword = BCrypt.hashpw(password, salt);

        System.out.println("securePassword: " + securePassword);

        Boolean match = BCrypt.checkpw(password, securePassword);

        System.out.println("match? : " + match);
    }
}