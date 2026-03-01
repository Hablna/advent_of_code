"""//package org.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class day2025 {
    //String filePath = "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";
    String filePath = "C:\\Users\\habib\\IdeaProjects\\First_project\\src\\entree";

    public ArrayList<String> day2025() {
        ArrayList listBanks = new ArrayList();

        try (FileReader fileReader = new FileReader(filePath);
             BufferedReader bufferedReader = new BufferedReader(fileReader)){
            String line;
            while ((line = bufferedReader.readLine()) != null){
                listBanks.add(line);
            }

        }catch (Exception e){
            System.out.println(e);
        }
        return listBanks;
    }

    public Integer day3() {
        int sum = 0;
        ArrayList<String> banks = day2025();
        for ( String bank : banks ){
            int combinaison = 0;
            for (int i = 0; i < bank.length(); i++){
                for (int j = i + 1; j < bank.length(); j++){
                    //differentes combinaison: de la valeur courante jusqu'à la fin
                    int newCombin = Integer.parseInt(String.valueOf(bank.charAt(i) +bank.charAt(j)));
                    if (newCombin > combinaison){
                        combinaison = newCombin;
                    }
                }
            }
            sum += combinaison;
        }
        return sum;

    }
}
