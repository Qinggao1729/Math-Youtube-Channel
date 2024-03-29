using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Instantiate512cubes : MonoBehaviour {

    // Prefab cube that gets spawned in.
	public GameObject cubePrefab;

    public static int totalCubes = SpectrumAnalyzer.totalCubes;

    public static int radius = 100;

	// Array that holds the 512 cubes we're spawning in.
	GameObject[] cubes = new GameObject[totalCubes];

    // Scales the height of each cube by this much.
	public float scale = 10000;

    public float rotationRate = 1;

    public float power = 1/2;

	/* Spawns 512 instances of cubePrefab in a circle of radius 100
     * around the object this script is attached to. Each cube is
     * rotated to face towards/away the center, and each cube is a
     * child of the object this script is attached to.
     */
	void Start () {
		for (int i = 0; i < 512; i++) {
            // Spawns a copy of cubePrefab.
            GameObject cube = Instantiate(cubePrefab);

			// Assigns this copy to it's proper position in cubes.
			cubes[i] = cube;

			// Names it properly.
			cube.name = "Cube" + i;

            // Set its parent to this object.
            cube.transform.parent = this.transform;


            cube.transform.eulerAngles = new Vector3(0, 360f / totalCubes * i, 0);
            cube.transform.position=cube.transform.forward* radius;


		}
	}
	
    void RotateCD(float amplitude)
    {
        float newY = Mathf.Pow(amplitude, power) * rotationRate;
        this.transform.Rotate(0.0f, newY, 0.0f);
    }
	/* Every frame, we'll take the data collected in SpectrumAnalyzer
     * and use it to set the heights of our cubes. Each of the 512 data
     * points our sample array corresponds to one of our cubes. Two caveats:
     *     1. FFT values are very small, so you'll want to scale each one up
     *        (use the scale variable).
     *     2. If a FFT value is 0, you don't want the cube to disappear, so
     *        add a small base height to every cube.
     */
	void Update () {
        RotateCD(Mathf.Max(SpectrumAnalyzer.freqBand));
        Debug.Log(Mathf.Max(SpectrumAnalyzer.freqBand));
        for (int i = 0; i < 512; i++) {
			if (cubes != null) {
                GameObject cube = cubes[i];

                float amplitude = SpectrumAnalyzer.samples[i];
                
                if (amplitude == 0)
                {
                    cube.transform.localScale = new Vector3(1, 0.005f, 1);
                }
                else
                {
                    cube.transform.localScale = new Vector3(1, amplitude * scale, 1);
                }

                

			}
		}
	}
}