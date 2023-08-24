using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cube : MonoBehaviour
{
    public int band;
    public float startScale=0.1f;
    public float scaleMultiplier=10;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        float audioAmplitude = SpectrumAnalyzer.audioBands[band];
        if (audioAmplitude == 0)
        {
            transform.localScale = new Vector3(10, startScale, 10);
        }
        else
        {
            transform.localScale = new Vector3(10, audioAmplitude * scaleMultiplier, 10);

        }


        
        
    }
}
