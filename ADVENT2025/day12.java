package org.example;

import java.nio.file.*;
import java.util.*;

public class day11 {

    static final String INPUT =
            "C:\\Users\\HALIROUNAMANOU-32255\\IdeaProjects\\test\\src\\main\\java\\org\\example\\entree";

    static List<List<int[][]>> orientations = new ArrayList<>(); // par forme : liste d'orientations (offsets)
    static List<Integer> shapeSize = new ArrayList<>();
    static int maxH = 0, maxW = 0;

    // État du backtracking
    static boolean[][] grid;
    static int[] remaining;
    static int H, W, slack;

    public static void main(String[] args) throws Exception {
        List<String> lines = Files.readAllLines(Path.of(INPUT));
        List<String[]> regions = new ArrayList<>();

        int i = 0;
        while (i < lines.size()) {
            String line = lines.get(i).trim();
            if (line.isEmpty()) { i++; continue; }
            if (line.matches("\\d+x\\d+:.*")) {
                regions.add(line.split(":"));
                i++;
            } else if (line.matches("\\d+:")) {
                List<String> rows = new ArrayList<>();
                i++;
                while (i < lines.size() && !lines.get(i).trim().isEmpty()
                        && !lines.get(i).trim().contains(":")) {
                    rows.add(lines.get(i).trim());
                    i++;
                }
                addShape(rows);
            } else i++;
        }

        int count = 0;
        for (String[] r : regions) {
            String[] dim = r[0].trim().split("x");
            int w = Integer.parseInt(dim[0]), h = Integer.parseInt(dim[1]);
            String[] q = r[1].trim().split("\\s+");
            int[] counts = new int[q.length];
            for (int k = 0; k < q.length; k++) counts[k] = Integer.parseInt(q[k]);
            if (fits(w, h, counts)) count++;
        }
        System.out.println("Partie 1 : " + count);
    }

    static void addShape(List<String> rows) {
        List<int[]> cells = new ArrayList<>();
        for (int r = 0; r < rows.size(); r++)
            for (int c = 0; c < rows.get(r).length(); c++)
                if (rows.get(r).charAt(c) == '#') cells.add(new int[]{r, c});
        shapeSize.add(cells.size());
        maxH = Math.max(maxH, rows.size());
        maxW = Math.max(maxW, rows.get(0).length());

        Set<String> seen = new HashSet<>();
        List<int[][]> list = new ArrayList<>();
        for (int t = 0; t < 8; t++) {
            List<int[]> tr = new ArrayList<>();
            for (int[] p : cells) {
                int r = p[0], c = p[1];
                for (int k = 0; k < t % 4; k++) { int tmp = r; r = c; c = -tmp; } // rotation 90°
                if (t >= 4) c = -c;                                               // miroir
                tr.add(new int[]{r, c});
            }
            // Ancrage sur la première cellule en ordre ligne/colonne
            tr.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
            int r0 = tr.get(0)[0], c0 = tr.get(0)[1];
            int[][] off = new int[tr.size()][];
            StringBuilder key = new StringBuilder();
            for (int k = 0; k < tr.size(); k++) {
                off[k] = new int[]{tr.get(k)[0] - r0, tr.get(k)[1] - c0};
                key.append(off[k][0]).append(',').append(off[k][1]).append(';');
            }
            if (seen.add(key.toString())) list.add(off);
        }
        orientations.add(list);
    }

    static boolean fits(int w, int h, int[] counts) {
        int presents = 0, need = 0;
        for (int k = 0; k < counts.length; k++) {
            presents += counts[k];
            need += counts[k] * shapeSize.get(k);
        }
        if (need > w * h) return false;                          // pas assez de cases
        if ((w / maxW) * (h / maxH) >= presents) return true;     // chaque cadeau dans sa propre case 3x3

        // Cas ambigu : vrai backtracking
        H = h; W = w;
        grid = new boolean[h][w];
        remaining = counts.clone();
        slack = w * h - need;
        return solve(0);
    }

    // Première case vide : soit on y ancre un cadeau, soit on la laisse vide (si slack > 0)
    static boolean solve(int pos) {
        boolean done = true;
        for (int r : remaining) if (r > 0) { done = false; break; }
        if (done) return true;

        while (pos < H * W && grid[pos / W][pos % W]) pos++;
        if (pos == H * W) return false;
        int r = pos / W, c = pos % W;

        for (int s = 0; s < remaining.length; s++) {
            if (remaining[s] == 0) continue;
            for (int[][] o : orientations.get(s)) {
                if (!canPlace(o, r, c)) continue;
                set(o, r, c, true);
                remaining[s]--;
                if (solve(pos + 1)) return true;
                remaining[s]++;
                set(o, r, c, false);
            }
        }
        if (slack > 0) {
            grid[r][c] = true; slack--;
            if (solve(pos + 1)) return true;
            grid[r][c] = false; slack++;
        }
        return false;
    }

    static boolean canPlace(int[][] o, int r, int c) {
        for (int[] d : o) {
            int rr = r + d[0], cc = c + d[1];
            if (rr < 0 || rr >= H || cc < 0 || cc >= W || grid[rr][cc]) return false;
        }
        return true;
    }

    static void set(int[][] o, int r, int c, boolean v) {
        for (int[] d : o) grid[r + d[0]][c + d[1]] = v;
    }
}
