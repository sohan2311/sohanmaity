
    import java.util.Scanner;
    public class Login {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String username = "admin";
        String password = "password";

        System.out.println("===== Login Page =====");
        System.out.print("Enter username: ");
        String enteredUsername = input.nextLine();

        System.out.print("Enter password: ");
        String enteredPassword = input.nextLine();

        if (enteredUsername.equals(username) && enteredPassword.equals(password)) {
            System.out.println("Login successful!");
            // Add your code for what should happen after successful login
        } else {
            System.out.println("Invalid username or password. Please try again.");
        }

        input.close();
    }
}


