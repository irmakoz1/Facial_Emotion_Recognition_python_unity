using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Emotion_Text : MonoBehaviour
{
    public TMPro.TMP_Text emotion_data;   
    private string emotion_s;
     // Start is called before the first frame update
 

    // Update is called once per frame
    void Update()
    {
        if( UdpSocket.emotion!= null)
        {
        emotion_s= UdpSocket.emotion;
        emotion_data.text=emotion_s;
        }
        else
        {
        emotion_s= "Waiting to Receieve Data";
        emotion_data.text =emotion_s ;       
        }
    }
}
