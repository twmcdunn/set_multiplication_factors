import java.util.ArrayList;
import java.util.Collections;

public class examples {

    public static ArrayList<ArrayList<Integer>> allPossibleChords(ArrayList<Integer> chord) {
        // if the input is already 3 notes, you're done!
        if (chord.size() == 3) {
            Collections.sort(chord);
            ArrayList<ArrayList<Integer>> chords = new ArrayList<ArrayList<Integer>>();
            return chords;
        }

        // an array to hold the 'completed chords'
        // (3 note chords)
        ArrayList<ArrayList<Integer>> compChords = new ArrayList<ArrayList<Integer>>();

        // get the highest note in the input chord
        int highestNote = 0;
        for (int note : chord) {
            highestNote = Math.max(highestNote, note);
        }

        // go up the chromatic scale, starting just
        // above the highest note in the input chord
        for (int i = highestNote + 1; i < 12; i++) {
            /*
             * if the note in question isn't in the chord
             * make a copy of the chord with this note added
             * pass the copy as input to this function itself
             * add the results of this to the completed chords array
             */
            if (!chord.contains(i)) {
                ArrayList<Integer> chordCopy = new ArrayList<Integer>();
                chordCopy.addAll(chord);
                chordCopy.add(i);
                compChords.addAll(allPossibleChords(chordCopy));
            }
        }
        return compChords;
    }

    public ArrayList<ArrayList<int[]>> allPossibleChordProgressions(
            int[] chordA, int[] chordB, ArrayList<int[]> progression) {
        /*
         * if the length of the progression is equal to the
         * number of notes in the chord you're multiplying out
         * then you're done!
         */
        if (progression.size() == chordA.length) {
            ArrayList<ArrayList<int[]>> progressions = new ArrayList<ArrayList<int[]>>();
            progressions.add(progression);
            return progressions;
        }

        // an array to hold the results
        ArrayList<ArrayList<int[]>> allPossibleProgressions;

        /*
         * create a copy of the progression, adding chord A as the
         * next chord. (It needs to be transposed so it's root is the
         * next note in the chord.)
         */
        ArrayList<int[]> option1 = new ArrayList<int[]>();
        option1.addAll(progression);
        option1.add(transpose(chordA, chordA[progression.size()]));

        // pass this progression as input and find all possible progressions
        // for the remaining chord members
        allPossibleProgressions = allPossibleChordProgressions(chordA, chordB, option1);

        // do the same thing as above, but assigning chord B as the
        // next chord in the progression
        ArrayList<int[]> option2 = new ArrayList<int[]>();
        option2.addAll(progression);
        option2.add(transpose(chordB, chordA[progression.size()]));
        allPossibleProgressions.addAll(allPossibleChordProgressions(chordA, chordB, option2));

        return allPossibleProgressions;
    }

    public int[] transpose(int[] chord, int interval) {
        return null;
    }
}