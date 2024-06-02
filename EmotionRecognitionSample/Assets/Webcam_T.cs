using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Webcam_T : MonoBehaviour
{
    // Start is called before the first frame update
    [SerializeField]
    private UnityEngine.UI.RawImage _rawImage;

    void Start()
    {
        WebCamDevice[] devices = WebCamTexture.devices;

        // for debugging purposes, prints available devices to the console
        for (int i = 0; i < devices.Length; i++)
        {
            print("Webcam available: " + devices[i].name);
        }
        
        WebCamTexture tex = new WebCamTexture(devices[1].name);

        this._rawImage.texture = tex;
        tex.Play();
        //Renderer rend = this.GetComponentInChildren<Renderer>();

        // assuming the first available WebCam is desired

       // rend.material.mainTexture = tex;
       
}
    
}
