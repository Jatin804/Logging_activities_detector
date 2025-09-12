Here are the details of each paper, including their main contributions and main limitations, based on the provided sources:

---

### 1. Khan, A., Ali, H., Jadoon, M., Abideen, Z., Minuallah, N. (2024). "Combatting Illegal Logging with AI-powered IoT Devices for Forest Monitoring"

**Main Contributions:**
*   This research presents a **comprehensive strategy for tackling illegal logging** by leveraging Artificial Intelligence (AI) and Internet of Things (IoT) technologies.
*   **IoT devices equipped with sensors** are used to continuously monitor and detect surrounding sounds in high-risk forestry areas.
*   An **AI component utilizes machine learning methods** to accurately identify and distinguish sound patterns associated with unlawful logging activities, such as chainsaw and tree cutting operations, and to detect natural disasters like wildfires.
*   Upon detection of such activities by these smart AI-powered IoT devices, **real-time notifications** are generated, enabling prompt intervention by enforcement agencies like the forest department.
*   The strategy aims to support **biodiversity preservation and sustainable forest management** by providing targeted and prompt solutions.
*   The proposed methodology uses **low-power microcontrollers** like the ESP32 (a system-on-chip with integrated Wi-Fi and Bluetooth) as sensor nodes.
*   Audio data is recorded using an **INMP441 omnidirectional MEMS microphone**.
*   **Mel-filter bank energy features (MEF)** are chosen for audio classification, extracted using the Edge Impulse Platform.
*   A **Convolutional Neural Network (CNN) model** is trained to classify audio into four classes: Silence, Axe, Chainsaw, and Fire. The network architecture includes an input layer (3,960 features), reshape layer (40 columns), two 1D Conv/Pool layers (8 and 16 neurons respectively), two Dropout layers (Rate 0.25), a Flatten Layer, an Additional Layer, and an output layer for 4 classes.
*   The model achieved a **96.2% accuracy** on the validation set with a low loss of 0.10.
*   In testing scenarios, the model demonstrated an **overall accuracy of 82.57%**, successfully classifying audio samples into groups, including instances of uncertainty.
*   On-device performance showed **efficient inferencing** taking only 21 milliseconds (MS), with minimal resource usage: 10.6KB peak RAM and 32.6KB flash usage on the ESP32 SoC.
*   **LoRa communication** is employed for secure transmission of identified voices and node locations (longitude, latitude) from the sensor nodes to a central server node (another ESP32).
*   The server node integrates with **Firebase**, a Google cloud platform, for real-time data storage, updating node locations, and maintaining a centralized and accessible data repository.
*   A **mobile application** is built to interface with the Firebase database, providing real-time notifications to users such as local communities, law enforcement, and environmental groups.

**Main Limitations:**
*   The provided sources do not explicitly state any limitations for this specific proposed system. The paper highlights the system's "spectacular accuracy" and "suitability for real-world deployment" without discussing its shortcomings.

---

### 2. XyloTron (Wikipedia Article)

**Main Contributions:**
*   The **XyloTron is an open-source, portable wood identification system** developed to support the enforcement of laws against illegal logging.
*   It utilizes **machine vision and artificial intelligence (AI)** to classify wood specimens based on their macroscopic anatomical features.
*   The device is designed for use in both **laboratory and field settings**, offering a non-destructive method of wood species identification.
*   It operates by capturing standardized images of a wood surface using a digital camera and controlled lighting, then comparing the sample against a model trained on verified reference specimens.
*   Both the hardware and software of the system are **open-source**.
*   A significant advantage is its ability to **work offline**, making it suitable for deployment in remote field locations where internet access is unavailable.
*   Field trials conducted in South America, Southeast Asia, and Africa have demonstrated its effectiveness in **intercepting timber suspected to be illegally harvested**.
*   Initial conceptual work began around 2018 at the United States Forest Products Laboratory (FPL).

**Main Limitations:**
*   The **accuracy of the system depends on the quality of the training data** and the similarity of samples to those included in the model.
*   For **high-stakes legal enforcement or forensic confirmation, microscopic analysis by a trained wood anatomist may still be required**. This indicates that while useful, it may not be a definitive standalone tool for all legal contexts.

---

### 3. Ahmed, A.M., Hussaini, S.S.A., Rahman, S.A., Azeemuddin, S. (2025). "Cyber-Driven Surveillance and Alert System for Illegal Logging Detection in Protected Forest Areas"

**Main Contributions:**
*   Proposes a **novel cyber-driven surveillance and alert system** designed for real-time detection and reporting of illegal logging activities in protected forest zones.
*   The system integrates **Internet of Things (IoT) sensors, edge computing, and artificial intelligence (AI)** for continuous environmental monitoring.
*   It employs both **acoustic sensors to detect chainsaw sounds** and **visual sensors to capture unauthorized human activity**.
*   **AI algorithms** are used to classify detected threats and generate alerts for forest officials, transmitted via secure communication protocols.
*   The methodology involves training a **Convolutional Neural Network (CNN)** model with audio datasets for chainsaw sound detection.
*   **Object detection models (YOLOv5)** are trained to recognize unauthorized persons in restricted zones using visual sensor data.
*   Field deployment across a 5 km² area in a wildlife reserve with 10 sensor nodes demonstrated high performance.
*   Experimental results showed a detection accuracy of **96.2% for acoustic logging events** and **91.5% for visual detection**.
*   Alerts were generated with an average **latency of 3.8 seconds**.
*   The system significantly **reduced response times and improved event traceability** compared to traditional manual patrols.
*   A **mesh network ensures sensor connectivity** even in dense foliage, and **encrypted communication maintains data integrity**.

**Main Limitations:**
*   Challenges encountered during field tests included **sensor weatherproofing**.
*   The system faced issues with **wildlife-triggered false positives**, which were mitigated through model refinement and sensor casing improvements.
*   Future enhancements proposed by the authors include **drone-assisted validation, integration with satellite data, and broader deployment** across ecologically sensitive regions, suggesting these are current areas for development.

---

### 4. Mujetahid, A., Nursaputra, M., Soma, A.S. (2023). "Monitoring Illegal Logging Using Google Earth Engine in Sulawesi Selatan Tropical Forest, Indonesia"

**Main Contributions:**
*   This research addresses the issue of forest destruction and illegal logging in Indonesia, which is often only discovered after the timber products have been distributed, highlighting the **lack of comprehensive forest monitoring**.
*   It proposes using **remote sensing technology, specifically Google Earth Engine (GEE)**, developed on the basis of artificial intelligence and machine learning, to monitor illegal logging events.
*   The study analyzes illegal logging using **Sentinel 1 SAR and Sentinel 2 Multispectral data**. The use of Sentinel 1's radar sensor is particularly crucial for tropical regions like Indonesia, where it can penetrate clouds, enabling observation of forest conditions even with cloud cover.
*   A **Random Forest classification algorithm** on the GEE platform is utilized to map forest conditions and identify changes.
*   Data on forest conditions in Sulawesi Selatan Province for 2021 were obtained, covering an area of **2,843,938.87 ha (63% of the province's total area)**.
*   The identification of illegal logging events found **1971 spots of forest change** between January–April and April–August, and **1680 spots of forest change** between April–August and September–December, revealing a total incident area of **7599.28 ha**.
*   The identification results showed a high conformity with secondary data from field monitoring by relevant agencies, achieving a **kappa accuracy value of 0.89**. The overall accuracy was 95.80%.
*   The technology provides a method for **early monitoring of illegal logging locations** and can serve as a basis for field monitoring by policymakers to prioritize patrols in high-incidence areas.
*   The study highlights GEE as a tool that can empower the wider community to report environmental damage.

**Main Limitations:**
*   Traditional surveillance mechanisms in Indonesia, such as routine patrols, are hampered by **limited human resources and insufficient budget**. While GEE offers a solution to this, it acknowledges the existing problem.
*   **Field surveys and direct validation of all outputs were generally impossible** due to the large area; reference data for accuracy testing was obtained from the Sulawesi Region Environmental and Forestry Law Enforcement Centre.
*   The method focuses on **detecting changes in forest cover** over periods rather than providing real-time alerts or immediate intervention capabilities, making it more of a retrospective monitoring tool for strategic planning.

---

### 5. Mutiara, G.A., Herman, N.S., Mohd, O. (2020). "Using Long-Range Wireless Sensor Network to Track the Illegal Cutting Log"

**Main Contributions:**
*   This paper proposes an **integrated system of IoT and Wireless Sensor Networks (WSN)** to identify and track the position of a moving cutting log, aiming to combat illegal logging and support forest preservation.
*   The system is designed to **reduce the burden on forest guards** by enabling remote monitoring and supervision of trees.
*   The hardware components include an **Arduino Uno, Raspberry Pi 3 B+, a sound sensor, an accelerometer sensor, a LoRa GPS HAT Shield, and an Outdoor LoRa Gateway OLG01**.
*   A **gyro accelerometer sensor detects the slope of tree trunks**, and a **sound sensor detects chainsaw sounds**.
*   It leverages **LoRa (Long-Range) communication** and the LoRaWAN open protocol, a Low-Power Wide-Area Network (LPWAN), which provides wide area coverage and low battery consumption, addressing the limitations of shorter-range technologies like ZigBee.
*   The network architecture follows a **STAR of STAR topology**.
*   Illegal logging is detected when both the **sound sensor exceeds a predetermined threshold** and the **accelerometer data indicates a change in tree position**.
*   The system provides **GPS position information of the moving log to forest police** through a web application and Telegram.
*   **LoRa communication performance**: In Line of Sight (LoS) areas, sensor nodes connected to the gateway within a range of **0–900 m** for one node and **0–750 m** for another. In Non-Line of Sight (N-LoS) urban small forest areas, the range was **0–350 m**, and in N-LoS suburb forest areas, it was **0–300 m**.
*   The optimal placement for sensor nodes and gateways is estimated at **1.8 to 2 meters from the ground**.
*   **Tracking performance**: In LoS conditions, information delivery was **real-time (2–5 seconds)**. In N-LoS conditions, processing time ranged from **20–34 seconds** in a small forest and **5–46 seconds** in a suburb forest.
*   **Energy consumption**: Estimated battery life for the system without GPS tracking is **195.9 hours**. When GPS is actively tracking, battery life is reduced to **140.95 hours**.

**Main Limitations:**
*   Prior satellite imagery systems for illegal logging **lack real-time tracking and reporting** capabilities and require higher computational power. This paper aims to overcome these limitations.
*   Existing WSN solutions using ZigBee have **weaknesses in communication coverage area and network infrastructure** for wide-area applications.
*   In **N-LoS areas, the communication range is significantly shorter** due due to obstacles like dense trees and high buildings.
*   Information delivery in **N-LoS areas is not always real-time**, taking up to 46 seconds, which is slower than LoS conditions.
*   **GPS functionality consumes significant energy**, leading to a faster depletion of battery life during active tracking.
*   The **energy consumption of the LoRa/GPS HAT for Raspberry Pi is "not optimal"**; it is suggested that replacing components with other LoRa series compatible with Arduino could improve optimization.
*   While an **extra antenna could extend the range**, this would increase energy consumption, which needs careful consideration.
*   The current prototype is relatively small, and future work suggests building a **larger prototype** embedded into a whole logging process stage.
*   Enhancements in **GPS-free geolocation** are proposed for future work.
*   Further exploration of **efficient energy consumption at each node sensor** is needed for wide-area network deployments.

---

### 6. Andreadis, A., Giambene, G., Zambon, R. (2021). "Monitoring Illegal Tree Cutting through Ultra-Low-Power Smart IoT Devices"

**Main Contributions:**
*   The paper proposes and evaluates a framework for **automatically detecting illegal tree-cutting activity and fire** in forests through audio event classification.
*   It envisages the use of **ultra-low-power tiny IoT devices** embedding edge-computing microcontrollers and long-range wireless communication (LoRa) to cover vast forest areas.
*   An **efficient and accurate audio classification solution based on Convolutional Neural Networks (CNNs)** is proposed, specifically designed for resource-constrained wireless edge devices.
*   The system can recognize a **wider range of threats** including handsaws, chainsaws, and fire sounds, through a distributed and pervasive edge-computing technique, differentiating it from previous works often limited to chainsaw detection.
*   It achieved an **accuracy of 85%** in detecting and notifying tree-cutting events.
*   **Edge computing is performed directly on the IoT node**, meaning feature extraction and audio classification by the neural network happen on the device. This minimizes the amount of data transmitted over the wireless network, significantly reducing energy consumption.
*   The lightweight neural network is implemented on an **ARM-Cortex M4F-powered device with only 256 kB of RAM**, making it highly resource-efficient.
*   Different pre-processing techniques were evaluated, and **Mel Frequency Cepstral Coefficients (MFCC)** was identified as the best trade-off for low RAM usage and good processing time.
*   The adoption of **8-bit integer quantization** (instead of 32-bit floating-point) for audio acquisition and processing provided a significant reduction in computational, memory, and energy resources (e.g., 4.5x faster inferencing, 3.8x less peak RAM, 2x less ROM) with a negligible loss of accuracy (MFCC-8 achieved 85.03% vs MFCC-32 at 85.37%).
*   **LoRa wireless communication performance**: It achieved a coverage radius of **more than 8 km in Line of Sight (LoS)** scenarios and **more than 2.5 km in light Non-Line of Sight (NLoS)** scenarios. However, in dense woods, the coverage radius was **less than 1 km**.
*   The device demonstrated remarkable energy efficiency, performing **over 61 hours of continuous sound monitoring and classification** with an 1800 mAh 3.7 V battery, assuming tree-cutting is a rare event. This paves the way for photovoltaic-based charging for low-maintenance deployments.
*   The overall processing time (from sound digitalization to final classification) for the most promising solution (MFCC pre-processing with 8-bit quantization) is **1160 ms**.

**Main Limitations:**
*   The audio recognition tests were exclusively performed using **recorded sounds from the ESC dataset**, rather than real sounds emitted by chainsaws, handsaws, or fires in a live forest environment.
*   The experimental testbed involved measurements only in **small wood areas** within a rural scenario and under **sunny weather conditions**.
*   There is a need for **extensive simulations and deeper empirical validation** of the LoRa module's transmission performance under various weather conditions (e.g., rain, snow, wind, fog) and different vegetation scenarios (e.g., tropical jungle, conifer mountain forests) to gain a more accurate understanding of LoRa coverage in diverse real-life settings.
*   Achieving lower detection times would require more powerful hardware, which would **inevitably lead to greater power consumption** and might not be suitable for the goal of low-power, long-term remote operation.
*   While the tree-cutting detection scenario does not have stringent time constraints, **packet retransmissions in LoRa can introduce latency** in message delivery.
*   **Vegetation and other obstacles (buildings, hills) introduce heavy signal degradation** in LoRa communication, significantly reducing the communication range in dense woods or NLoS scenarios.
