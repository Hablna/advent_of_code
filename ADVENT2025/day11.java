package org.example;

import java.nio.file.*;
import java.util.*;

public class day11 {

    static final String INPUT =
            "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";

    static Map<String, List<String>> graph = new HashMap<>();
    static Map<String, Long> memo = new HashMap<>();

    public static void main(String[] args) throws Exception {
        for (String line : Files.readAllLines(Path.of(INPUT))) {
            line = line.trim();
            if (line.isEmpty()) continue;
            String[] parts = line.split(":");
            String from = parts[0].trim();
            List<String> outs = new ArrayList<>();
            for (String s : parts[1].trim().split("\\s+"))
                if (!s.isEmpty()) outs.add(s);
            graph.put(from, outs);
        }

        // Partie 1 : chemins de "you" à "out"
        long part1 = graph.containsKey("you") ? count("you", true, true) : 0;

        // Partie 2 : chemins de "svr" à "out" passant par "dac" ET "fft"
        memo.clear();
        long part2 = graph.containsKey("svr") ? count("svr", false, false) : 0;

        System.out.println("Partie 1 : " + part1);
        System.out.println("Partie 2 : " + part2);
    }

    // Nombre de chemins de node à "out", en suivant si dac / fft ont été visités
    static long count(String node, boolean dac, boolean fft) {
        if (node.equals("dac")) dac = true;
        if (node.equals("fft")) fft = true;
        if (node.equals("out")) return (dac && fft) ? 1 : 0;

        String key = node + "|" + dac + "|" + fft;
        Long cached = memo.get(key);
        if (cached != null) return cached;

        long total = 0;
        for (String next : graph.getOrDefault(node, List.of()))
            total += count(next, dac, fft);

        memo.put(key, total);
        return total;
    }
}
