package org.example;

import java.nio.file.*;
import java.util.*;
import java.util.regex.*;

public class Day10 {

    static final String INPUT =
            "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";

    public static void main(String[] args) throws Exception {
        long part1 = 0, part2 = 0;
        for (String line : Files.readAllLines(Path.of(INPUT))) {
            line = line.trim();
            if (line.isEmpty()) continue;
            Machine m = new Machine(line);
            part1 += m.part1();
            part2 += m.part2();
        }
        System.out.println("Partie 1 : " + part1);
        System.out.println("Partie 2 : " + part2);
    }

    static class Machine {
        static final long INF = Long.MAX_VALUE / 4;
        static final Pattern BTN = Pattern.compile("\\(([^)]*)\\)");

        int n;            // nombre de lumières / compteurs
        int lightMask;    // diagramme cible (partie 1)
        int[] target;     // joltages cibles (partie 2)
        int[][] effect;   // effet de chaque sous-ensemble de boutons (appuyés 1 fois)
        int[] size;       // nombre de boutons dans le sous-ensemble
        Map<Integer, List<Integer>> byParity = new HashMap<>();
        Map<String, Long> memo = new HashMap<>();

        Machine(String line) {
            // Lumières
            String lights = line.substring(line.indexOf('[') + 1, line.indexOf(']'));
            n = lights.length();
            for (int i = 0; i < n; i++)
                if (lights.charAt(i) == '#') lightMask |= 1 << i;

            // Boutons
            List<int[]> buttons = new ArrayList<>();
            Matcher mt = BTN.matcher(line);
            while (mt.find()) {
                String[] parts = mt.group(1).split(",");
                int[] b = new int[parts.length];
                for (int i = 0; i < parts.length; i++) b[i] = Integer.parseInt(parts[i].trim());
                buttons.add(b);
            }

            // Joltages
            String[] j = line.substring(line.indexOf('{') + 1, line.indexOf('}')).split(",");
            target = new int[j.length];
            for (int i = 0; i < j.length; i++) target[i] = Integer.parseInt(j[i].trim());

            // Pré-calcul de tous les sous-ensembles de boutons
            int B = buttons.size();
            int total = 1 << B;
            effect = new int[total][];
            size = new int[total];
            effect[0] = new int[n];
            for (int s = 1; s < total; s++) {
                int low = Integer.numberOfTrailingZeros(s);
                int prev = s & (s - 1);
                effect[s] = effect[prev].clone();
                for (int idx : buttons.get(low)) effect[s][idx]++;
                size[s] = size[prev] + 1;
            }
            for (int s = 0; s < total; s++)
                byParity.computeIfAbsent(parity(effect[s]), k -> new ArrayList<>()).add(s);
        }

        static int parity(int[] v) {
            int m = 0;
            for (int i = 0; i < v.length; i++) if ((v[i] & 1) == 1) m |= 1 << i;
            return m;
        }

        // Partie 1 : appuyer 2 fois = ne rien faire, donc chaque bouton 0 ou 1 fois
        long part1() {
            long best = INF;
            for (int s : byParity.getOrDefault(lightMask, List.of())) best = Math.min(best, size[s]);
            return best;
        }

        long part2() {
            return solve(target);
        }

        // x = p + 2y : p (0/1 par bouton) fixe la parité, puis on résout la moitié restante
        long solve(int[] t) {
            boolean zero = true;
            for (int v : t) if (v != 0) { zero = false; break; }
            if (zero) return 0;

            String key = Arrays.toString(t);
            Long cached = memo.get(key);
            if (cached != null) return cached;

            long best = INF;
            for (int s : byParity.getOrDefault(parity(t), List.of())) {
                int[] e = effect[s];
                int[] half = new int[n];
                boolean ok = true;
                for (int i = 0; i < n; i++) {
                    if (e[i] > t[i]) { ok = false; break; }
                    half[i] = (t[i] - e[i]) / 2;
                }
                if (!ok) continue;
                long r = solve(half);
                if (r < INF) best = Math.min(best, size[s] + 2 * r);
            }
            memo.put(key, best);
            return best;
        }
    }
}
