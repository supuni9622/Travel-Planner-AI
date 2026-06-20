Your goal is to identify and update any vulnerable dependencies.

Do the following.
1. Run `pip audit` to find the vulnerable installed packages in the project. 
2. Run `pip audit fix` to apply updates
3. Run tests and verify the updates didn't break anything
4. Run `pip freeze > requirements.txt` to update the requirements file with updated package details