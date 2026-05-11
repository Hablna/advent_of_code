"""

"""package org.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


public class day2025 {
    String filePath = "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";
    //String filePath = "C:\\Users\\habib\\IdeaProjects\\First_project\\src\\entree";

    public List<List<String>> readFile() {
        List<String> plageId = new ArrayList<>();
        List<String> Ids = new ArrayList<>();
        boolean isPlgeId = true;

        List<List<String>> input = new ArrayList<>();

        try (FileReader fileReader = new FileReader(filePath);
             BufferedReader bufferedReader = new BufferedReader(fileReader)){
            String line = new String();

            while (( line = bufferedReader.readLine())!= null){
                if (line.isBlank()){
                    isPlgeId = false;
                    continue;
                }

                (isPlgeId?plageId: Ids).add(line);
            }
            input.add(plageId);
            input.add(Ids);

        }catch (Exception e){
            System.out.println(e);
        }
        return input;
    }

    public Integer totalFreshId(){
        List<List<String>> input = readFile();
        List<String> plageId = input.getFirst();
        List<String> Ids = input.get(1);

        Set<Long> intPlageIds = new HashSet<>();

        for (String plage: plageId){
            String[] minmax = plage.split("-");
            for (Long i = Long.parseLong(minmax[0]); i<=Long.parseLong(minmax[1]); i++){
                intPlageIds.add(i);
            }
        }

        int count = 0;
        for (String id : Ids){
            if (intPlageIds.contains(Long.parseLong(id))){
                count++;
            }
        }
        return count;
    }

}
