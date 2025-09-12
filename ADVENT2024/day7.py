#Enjava

'''
package org.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import static java.lang.Long.parseLong;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        String filePath = "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";
        try (FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader)) {
            String line;
            Long somme = 0L;
            while ((line = bufferedReader.readLine()) != null) {
                String[] equation = ((line.split(":"))[1].strip()).split(" ");
                long target;
                target = parseLong(((line.split(":"))[0].strip()));

                List<Long> numbers = new ArrayList<>();
                for (String eq: equation)
                    numbers.add(parseLong(eq));

                if (canReach(target, numbers)){
                    somme+=target;
                }
            }
            System.out.println(somme);
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    public static boolean canReach(Long target, List<Long> equation){
        if (equation.size() == 1)
            return Objects.equals(equation.getFirst(), target);

        Long num1 = equation.getFirst();
        Long num2 = equation.get(1);
        List<Long> rest = equation.subList(2, equation.size());

        //multiplication
        List<Long> mulList = new ArrayList<>();
        mulList.add(num1 * num2);
        mulList.addAll(rest);

        if (canReach(target, mulList))
            return true;
        //addition
        List<Long> addList = new ArrayList<>();
        addList.add(num1 + num2);
        addList.addAll(rest);

        if (canReach(target, addList))
            return true;

        return false;
    }
}
'''