"""package org.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;

public class day2025 {
    String filePath = "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";
    //String filePath = "C:\\Users\\habib\\IdeaProjects\\First_project\\src\\entree";

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

    public Long day3() {
        Long sum = 0L;
        ArrayList<String> banks = day2025();
        for ( String bank : banks ){

            ArrayList<Integer> top12 = new ArrayList<>();
            ArrayList<Integer> intBank = new ArrayList<>();

            int length = bank.length();
            for (int i = 0; i<length; i++){
                intBank.add(Integer.parseInt(String.valueOf(bank.charAt(i))));
            }

            for (int j = 0; j < length; j++){
                if (top12.size() < 12 ){
                    top12.add(intBank.get(j));
                } else if (top12.size() == 12) {
                    if (Collections.min(top12) < intBank.get(j)){
                        top12.remove(Integer.valueOf(Collections.min(top12)));
                        top12.add(intBank.get(j));
                    }
                }
            }
            StringBuilder sb = new StringBuilder();
            for (int n : top12){
                sb.append(n);
            }

            sum += Long.parseLong(sb.toString());

        }
        return sum;

    }
}
