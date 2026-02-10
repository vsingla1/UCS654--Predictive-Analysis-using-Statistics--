# Text Generation Model Selection using TOPSIS

## 📌 Overview  
This project applies the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** multi-criteria decision-making method to select the **best pre-trained model for Prompt-based Text Generation**.  
Instead of selecting a model based on a single metric, multiple quality and efficiency criteria are considered to provide a balanced and practical ranking.

---

## 🎯 Task Definition  
**Task:** Prompt-based Text Continuation  

Given a fixed set of short prompts, each pre-trained language model generates a continuation. The generated outputs are evaluated using automatic metrics and system-level performance measures. The TOPSIS method is used to rank the models.

---

## 🧠 Models Compared  

The following six pre-trained models are evaluated:

- GPT-2  
- DistilGPT-2  
- BART-base  
- T5-small  
- GPT-Neo-125M  
- OPT-125M  

These models represent different architectures and sizes, capturing trade-offs between text quality and computational efficiency.

---

## 📊 Evaluation Criteria  

| Criterion           | Type     | Description |
|--------------------|----------|-------------|
| BLEU               | Benefit  | Measures n-gram overlap between generated text and reference |
| ROUGE-L            | Benefit  | Measures longest common subsequence similarity |
| BERTScore          | Benefit  | Measures semantic similarity using contextual embeddings |
| Perplexity         | Cost     | Measures fluency of the language model (lower is better) |
| InferenceTime (ms) | Cost     | Average generation time per sample |
| ModelSize (MB)     | Cost     | Memory footprint of the model |
| EaseOfFinetuning   | Benefit  | Practical ease of fine-tuning and usability (1–5 scale) |

---

## ⚖️ Criteria Weights  

The weights assigned to each criterion (sum = 1.0):

| Criterion           | Weight |
|--------------------|--------|
| BLEU               | 0.25   |
| ROUGE-L            | 0.20   |
| BERTScore          | 0.20   |
| Perplexity         | 0.15   |
| InferenceTime      | 0.10   |
| ModelSize          | 0.05   |
| EaseOfFinetuning   | 0.05   |

Quality-related metrics are given higher importance, while efficiency and usability metrics ensure practical feasibility.

---

## 🧮 Methodology (TOPSIS)

1. Performance metrics for each model are stored in `input_data.csv`.  
2. The decision matrix is normalized using vector normalization.  
3. Normalized values are multiplied by predefined weights.  
4. Positive ideal and negative ideal solutions are identified.  
5. Euclidean distances to the ideal solutions are computed.  
6. TOPSIS scores are calculated to determine relative closeness.  
7. Models are ranked based on TOPSIS scores.

---

## 📁 Project Structure 
.
├── input_data.csv
├── topsis_text_generation.py
├── topsis_results.csv
├── topsis_ranking.png
└── README.md

---

## ▶️ How to Run  

1. Install dependencies:
   ```bash
    pip install pandas numpy matplotlib
    python topsis_text_generation.py
   ```

## 📈 Results
The TOPSIS method was applied to six pre-trained text generation models using seven evaluation criteria: BLEU, ROUGE-L, BERTScore, Perplexity, Inference Time, Model Size, and Ease of Fine-tuning. The obtained rankings reflect a balanced trade-off between text generation quality and computational efficiency. Models achieving higher semantic similarity and n-gram overlap scores while maintaining reasonable inference time and manageable model size were ranked higher. The results are summarized numerically in topsis_results.csv and visually in topsis_ranking.png, enabling easy comparison of model performance across multiple dimensions.

## ✅ Conclusion
This work demonstrates that TOPSIS provides a structured and explainable framework for selecting pre-trained text generation models by integrating multiple evaluation criteria rather than relying on a single metric. The final ranking highlights the importance of balancing generation quality with practical deployment considerations such as speed and resource requirements. The same evaluation framework can be extended to other NLP tasks by adjusting the criteria and weights, making it a general-purpose approach for model selection in applied machine learning scenarios.