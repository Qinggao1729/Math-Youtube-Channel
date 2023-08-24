using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpectrumAnalyzer : MonoBehaviour
{
    AudioSource audioSource;
    public static int totalCubes = 512;
    public static int totalBands = 8;
    public static float[] samples = new float[totalCubes];
    public static float[] freqBand = new float[totalBands];
    float[] freqBandHighest = new float[totalBands];
    public static float[] audioBands = new float[totalBands];



    // Start is called before the first frame update
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }

    void GetSpectrumAudioSource()
    {
        audioSource.GetSpectrumData(samples, 0, FFTWindow.Blackman);

    }

    void MakeFrequencyBands()
    {
        int count = 0;

        // Iterate through the 8 bins.
        for (int i = 0; i < totalBands; i++)
        {
            float average = 0;
            int sampleCount = (int)Mathf.Pow(2, i + 1);

            // Adding the remaining two samples into the last bin.
            if (i == 7)
            {
                sampleCount += 2;
            }

            // Go through the number of samples for each bin, add the data to the average
            for (int j = 0; j < sampleCount; j++)
            {
                average += samples[count];
                count++;
            }

            // Divide to create the average, and scale it appropriately.
            average /= count;
            freqBand[i] = (i + 1) * 100 * average;
        }
    }

    void CreateAudioBands()
    {
        for (int i = 0; i < totalBands; i++)
        {
            if (freqBand[i] > freqBandHighest[i]){
                freqBandHighest[i] = freqBand[i];
            }
            

        }
        for (int i = 0; i < totalBands; i++)
        {
            audioBands[i] = freqBand[i]/freqBandHighest[i];
        }
    }

    // Update is called once per frame
    void Update()
    {
        GetSpectrumAudioSource();
        MakeFrequencyBands();
        CreateAudioBands();
    }
}
