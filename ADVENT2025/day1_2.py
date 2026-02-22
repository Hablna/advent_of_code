//package org.example;

"""import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day2025 {
    //String filePath = "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";
    String filePath = "C:\\Users\\habib\\IdeaProjects\\First_project\\src\\entree";

    public ArrayList<String> day2025() {
        ArrayList<String> instructions = new ArrayList<>();
        try(FileReader fl = new FileReader(filePath);
            BufferedReader bf = new BufferedReader(fl)){
            String line;

            while ((line = bf.readLine()) != null){
                instructions.add(line);
            }
        }catch(IOException e){
            System.out.println("erreur lecture: "+ e.getMessage());
        }
        return instructions;
    }

    public int calculPassword() {
        ArrayList instructions = day2025();
        int i=0;
        int password = 50;
        for (Object instruction : instructions) {
            Pattern pattern = Pattern.compile("([A-Z])(\\d+)");
            Matcher matcher = pattern.matcher(instruction.toString());
            if (matcher.find()){
                int nbr = Integer.parseInt(matcher.group(2));
                if ("R".equals(matcher.group(1))){
                    //Calcul du nombre de click pour atteindre le premier 0
                    int toZero = (password == 0)? 100 : 100-password;
                    if (nbr >= toZero){
                        i += 1 + (nbr - toZero)/100;
                    }

                    password = cycle(password, nbr);
                }else{
                    int toZero = (password == 0)?100: password;
                    if (nbr >= toZero){
                        i += 1 + (nbr - toZero)/100;
                    }

                    password = cycle(password, -nbr);
                }
            }

        }
        return i;
    }

    public int cycle(int actuel, int modif) {
        int max = 100;
        // On ajoute 'max' avant le dernier modulo pour gérer les soustractions
        return (actuel + modif % max + max) % max;
    }
}
