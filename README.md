# 💰 Bank Management System with Voice Assistance
This Bank Management System allows users to deposit, withdraw, and check their balance with PIN authentication. The system also features voice assistance using pyttsx3, which provides auditory feedback for a more engaging user experience.

## ✨ Features
Deposit Money: Securely deposit funds into your account.
Withdraw Money: Withdraw funds from your account if your balance allows.
Check Balance: Verify your current account balance at any time.
Voice Assistance: Get real-time auditory feedback on your transactions.
PIN Authentication: Secure the system with a PIN to protect your account.
## ⚙️ Technology Stack
Python: Core programming language.
pyttsx3: Provides text-to-speech functionality.
cv2 (OpenCV): While imported, it's currently unused and can be removed or used for future enhancements (e.g., camera integration).


 ## Interact with the system:
Follow the on-screen instructions and use the options:

1 for Deposit
2 for Withdraw
3 for Check Balance
4 to Exit
For security reasons, make sure to enter your PIN for all transactions.

## 🛠️ Configuration
PIN: The default PIN is set to 76321. You can change it in the script by modifying the pin variable.
Voice Feedback: The system will read your actions aloud. Please ensure your system supports audio playback for the pyttsx3 module.
### 📝 Example Usage
plaintext
Copy code
=============== Bank Management System ===============
Press
 1. Deposit
 2. Withdraw
 3. Check Balance
 4. Exit
-------------------------------------------------
Enter how you would like to proceed: 1
Please enter The Amount: 5000
Enter your PIN: 76321
You deposited 5000 rupees.
Your current balance is 5000 rupees.
