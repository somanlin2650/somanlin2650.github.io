---
title: "從反應到異質理性：認知連續體、湧現與文明—AI 螺旋"
date: 2026-10-01 14:11:00 +0800
lang: zh-TW
alternate_url: /en/posts/from-reaction-to-heterogeneous-rationality/
categories: [AI, 認知]
tags: [人工智慧, 認知科學, 複雜系統, 湧現, 理性, 直覺, 集體智慧, 神經科學, 認識論]
description: "一個跨越單細胞、神經系統、個體理性、群體文明與人工智慧的認知框架：反射、直覺與理性不是彼此割裂的模組，而可能是連續因果組織經由非線性累積、抽象與外化後形成的不同宏觀狀態。"
math: true
toc: true
comments: true
---

## 摘要
{: #summary }

「反射、直覺、理性」很容易被描述成三種截然不同的認知模式；「單細胞、簡單動物、人類、文明、人工智慧」也很容易被排列成一條從低級到高級的階梯。然而，這些分類很可能只是觀察者為了理解複雜現象而做的粗粒化。

更一般的圖像是：從細胞內的化學反應、單細胞的感覺—運動耦合、植物的電訊號、分散式神經網，到大型神經系統、個體推理、語言、文化、科學、電腦與人工智慧，都可以被看成某種**適應性因果組織**（adaptive causal organization）在不同尺度上的實現。它們的共同點不是都具有「理性」或「意識」，而是都能以自身的內部狀態承接外部與內部訊號，再讓這些狀態影響後續行為；當記憶、可塑性、整合、預測、抽象、遞迴、通訊與外部化能力持續增加時，系統會出現愈來愈複雜的宏觀行為。

底層變量可以是連續的，但行為並不必然線性增加。閾值、正負回饋、網路耦合、模組化與結構重組都可能使連續變化在宏觀上呈現近似離散的「階段」。因此，反射、直覺、理性、語言與集體智慧可以被理解成一張高維連續空間中的不同 regime，而不是由天然邊界切開的幾種物質。

更重要的是，一旦某個複雜過程能形成穩定的宏觀狀態，它就可能被更高一層系統當成新的簡單元件。大量感知可以被壓縮成「物體」，多步推理可以被壓縮成「直覺」，一代人的發現可以被壓縮成「公式」，一整套演算法可以被壓縮成一個函式呼叫。新的簡單元件再彼此組合，形成新的複雜性。

由此形成一個反覆向上的螺旋：

$$
\boxed{
\text{連續累積}
\rightarrow
\text{非線性湧現}
\rightarrow
\text{穩定抽象}
\rightarrow
\text{新可操作單元}
\rightarrow
\text{新的複雜組合}
}
$$

人類文明把這個循環推進到跨腦、跨世代的尺度；電腦則把部分顯式理性外包成可自動執行的機制；大型神經網路又重新把人類文化中大量外化的知識與操作壓縮進人工學習系統。未來 AI 若進一步形成自己的 representation、primitive 與 operator，則可能出現一套對 AI 而言自然簡單、對人類而言卻極度陌生的「異質理性」。

這將使認識論面臨一個新的問題：真正的智慧邊界，也許不在「能不能回答已知問題」，而在「能不能創造新的可表示空間，使原本無法被提出的問題第一次成為問題」。

## 一、分類的錯覺：世界常是連續的，行為卻看起來有界線
{: #s1 }

日常語言習慣以二分方式描述世界：

- 有反應／沒有反應；
- 有記憶／沒有記憶；
- 有理性／沒有理性；
- 健康／生病；
- 智慧／不智慧；
- 生物／機器；
- 人類思考／人工運算。

這些分類有實用價值，但分類邊界並不必然等於底層自然結構的邊界。

一個簡單例子是閾值反應。假設系統內部有一個連續變量 $$q$$，而可觀察行為 $$B$$ 近似：

$$
B(q)=\frac{1}{1+e^{-k(q-q_c)}}
$$

當 $$k$$ 很大時，$$q$$ 只要跨過 $$q_c$$ 附近一小段範圍，外部行為就會從幾乎沒有快速轉成幾乎完全出現。

觀察者看到的是：

$$
0\rightarrow 1
$$

底層卻可能只是：

$$
0.47\rightarrow0.48\rightarrow0.49\rightarrow0.50\rightarrow0.51
$$

這類機制不只存在於簡單閾值函數。動態系統中的 bifurcation、正回饋、同步化、競爭性抑制、hysteresis 與網路臨界現象，都可能讓緩慢改變的控制參數產生突然的宏觀狀態轉換。

神經科學確實存在以 criticality 描述腦動態的研究，但「大腦是否普遍工作在精確臨界點」仍有重要爭論。因此，認知連續體不需要依賴「所有智慧都是物理相變」這個強假設。較保守而足夠的一般命題是：

$$
\boxed{
\text{連續的底層變化}
+
\text{非線性交互作用}
\Rightarrow
\text{看似離散的宏觀能力}
}
$$

反射、直覺與理性之所以看起來像三種東西，不一定因為自然界真的畫了三條線，而可能因為不同連續能力在交互作用後形成了幾個容易辨認的宏觀 regime。

## 二、研究對象：從「認知系統」改為「適應性因果組織」
{: #s2 }

若研究範圍從單細胞延伸到文明與 AI，「認知系統」一詞容易過早假定某些對象已經具有 cognition；「agent」又容易暗示單一目標、意圖與清楚邊界；「系統」則過於寬泛。

因此，可使用一個工作概念：

> **適應性因果組織（adaptive causal organization）**：一組彼此作用、具有內部狀態的單元；外部與內部訊號能改變其狀態，而目前狀態會對未來狀態與環境產生結構性的因果影響。當組織進一步具備記憶、可塑性、預測、模型形成、跨單元通訊或外部化能力時，會逐步出現更接近通常所稱「認知」的行為。

最小形式可以寫成：

$$
x_{t+1}=F_{\theta_t}(x_t,e_t)
$$

其中：

- $$x_t$$：系統在時間 $$t$$ 的內部狀態；
- $$e_t$$：當下環境或外部輸入；
- $$F_{\theta_t}$$：由當前結構 $$\theta_t$$ 所決定的狀態轉換。

若系統還能影響外界：

$$
a_t=G_{\theta_t}(x_t,e_t)
$$

其中 $$a_t$$ 是動作、輸出或對環境的干預。

若經驗還會改變系統本身：

$$
\theta_{t+1}
=
U(\theta_t,x_t,e_t,a_t,e_{t+1})
$$

就出現最廣義的學習或適應。

這些式子不企圖把生命、心智與文明全部化約成同一組微觀方程，而是提供共同語言：不同尺度的組織可以使用完全不同的物理機制，卻共享「狀態—轉換—回饋—更新」這種抽象結構。

研究焦點於是可以從：

> 「它到底算不算有認知？」

轉移為：

> 「它能保存多少狀態？整合多長時間？能否改變自己的轉換規則？能否形成模型？能否把中間狀態傳給其他單元？能否對自身進行再建模？」

## 三、認知不是一條軸，而是一個高維連續空間
{: #s3 }

「從低到高的智能」仍然過於一維。

一個組織的能力至少同時取決於多個變量。可用一個概念性向量表示：

$$
\mathbf q
=
(M,\tau,P,I,H,A,R,E,B,\ldots)
$$

其中可以分別代表：

- $$M$$：可保存的內部狀態與記憶容量；
- $$\tau$$：時間整合範圍；
- $$P$$：可塑性與學習能力；
- $$I$$：跨單元資訊整合能力；
- $$H$$：模組與階層深度；
- $$A$$：抽象與壓縮能力；
- $$R$$：遞迴建模與自我模型能力；
- $$E$$：外化、傳輸與跨系統互通能力；
- $$B$$：輸入、輸出與內部通訊頻寬。

反射、直覺、理性、語言與集體智慧都不必是一個新器官，而可以是 $$\mathbf q$$ 落在不同區域時產生的宏觀現象。

例如，一個快速局部反射可能具有較短的時間整合範圍、低抽象深度與極低外化能力；專家直覺則可能具有高度學習過的內部 representation、極短的 online deliberation 與高速映射；顯式理性則需要 intermediate state 的保存、較長時間整合、compositional operation 與錯誤回退；集體理性又進一步要求不同 processor 之間能交換 state。

因此，比「理性／非理性」更一般的表述是：

> **理性是一個高維連續空間中的宏觀 regime，而不是突然插入系統中的一種新物質。**

## 四、在神經元之前，生命就已經具有複雜的控制
{: #s4 }

若把 cognition 的起點硬放在神經元，就會錯過生命系統早已具備的大量資訊處理與控制。

### 4.1 細菌化學趨性：分子網路可以實現近似工程控制
{: #s4-1 }

大腸桿菌的 chemotaxis 是最經典的例子之一。

細菌沒有神經系統，但能透過受體、蛋白訊號網路與鞭毛馬達，比較環境中的化學變化，調整 run-and-tumble 行為，增加朝向有利環境移動的機率。

E. coli chemotaxis 的 adaptation 甚至可以用 integral feedback control 理解：在持續刺激下，系統能逐漸恢復基線敏感度，使它在很寬的背景濃度範圍中持續感知「變化」，而不是只感知絕對值。

這意味著某些控制原理：

$$
\text{sensing}
\rightarrow
\text{state update}
\rightarrow
\text{feedback}
\rightarrow
\text{adaptation}
$$

遠早於神經系統。

這不必被稱為「理性」，甚至不必強行稱為「認知」，但它已經具有後來複雜認知會大量依賴的結構性元素。

### 4.2 草履蟲：一個細胞也能具有電興奮性與感覺—運動轉換
{: #s4-2 }

草履蟲是單細胞生物，卻能依機械、化學、光與溫度刺激改變游動。

其典型 avoidance reaction 由 Ca$$^{2+}$$-based action potential 觸發：膜電位變化使纖毛中的電壓閘控鈣離子通道開啟，進而改變纖毛擺動方向，使草履蟲短暫後退、轉向，再恢復前進。

重要的不是是否把這稱作「思考」，而是：

> **單一細胞已經能把感覺、膜電位、離子流與運動組成一個閉迴路，而不需要先有神經元與大腦。**

### 4.3 捕蠅草：連續累積可以產生近似二元的「決策」
{: #s4-3 }

捕蠅草沒有神經元，卻使用電訊號與 Ca$$^{2+}$$ dynamics 協調快速閉合。

典型情況下，兩次對 trigger hair 的機械刺激若在約 30 秒內發生，第二次刺激會讓細胞質 Ca$$^{2+}$$ 累積到與閉合相關的閾值；若第二次刺激來得太晚，第一次刺激造成的 Ca$$^{2+}$$ 訊號已經衰減，就不足以觸發閉合。

可概念化為：

$$
C(t)<C_c
\Rightarrow
\text{保持開啟}
$$

$$
C(t)\ge C_c
\Rightarrow
\text{閉合}
$$

這個例子完整展示了「連續底層—離散外觀」：

- Ca$$^{2+}$$ 濃度是連續變量；
- 訊號會隨時間衰減；
- 兩次刺激可以時間整合；
- 行為最後卻近似是開／關。

因此，「是否記得第一次刺激」、「是否作出決定」等人類語言會自然產生二分感，但底層未必存在一道對應的二分邊界。

參考：

- [Yi et al., Robust perfect adaptation in bacterial chemotaxis through integral feedback control](https://authors.library.caltech.edu/records/sa6bx-35q11)
- [Responding to Chemical Gradients: Bacterial Chemotaxis](https://pmc.ncbi.nlm.nih.gov/articles/PMC3320702/)
- [Integrative Neuroscience of Paramecium, a “Swimming Neuron”](https://www.eneuro.org/content/8/3/ENEURO.0018-21.2021)
- [Suda et al., Calcium dynamics during trap closure visualized in transgenic Venus flytrap](https://www.nature.com/articles/s41477-020-00773-1)
- [Hedrich & Kreuzer, Demystifying the Venus flytrap action potential](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19113)

## 五、神經元的出現不是一道「智能開關」
{: #s5 }

神經元提供了非常強大的快速、可塑性通訊機制，但「有神經元」不等於「認知突然誕生」。

黏菌 *Physarum polycephalum* 沒有神經系統，卻有大量研究討論其導航、選擇、habituation-like learning、空間記憶與適應行為。這些現象是否應被稱為 cognition 仍有哲學與定義爭議；但爭議本身就說明，把神經元當成一道絕對邊界並不理想。

更適合的圖像是：

$$
\text{chemical networks}
\rightarrow
\text{electrical excitability}
\rightarrow
\text{specialized signaling cells}
\rightarrow
\text{nerve nets}
\rightarrow
\text{centralized nervous systems}
$$

不同演化支系不必依相同次序完成全部步驟，也不代表後者必然「更高級」。重點是：通訊速度、範圍、可塑性與組織方式的改變，逐步擴大系統能協調的狀態空間。

參考：[Reid, Thoughts from the forest floor: a review of cognition in the slime mould *Physarum polycephalum*](https://link.springer.com/article/10.1007/s10071-023-01782-1)

## 六、水螅：沒有中央大腦，也能出現功能分化與行為序列
{: #s6 }

Hydra 是理解「連續體而非階梯」的重要案例。

水螅沒有集中式大腦或神經節，其神經元只有數百到數千個，分散在 nerve nets 中。然而 whole-animal calcium imaging 顯示，這些神經元並不是均質混成一團，而存在多個功能上不同、解剖上可分的 network，分別和 contraction、elongation、radial contraction、nodding 等行為相關。

更複雜的 locomotion，例如 somersault，也需要多個動作按照時間順序協調完成。

這說明：

$$
\text{distributed nerve net}
\not\Rightarrow
\text{只能做單一反射}
$$

即使在沒有中央大腦的架構中，也可以逐漸出現：

- 模組化；
- network specialization；
- sequence coordination；
- sensorimotor integration。

因此，「反射」與「多步行為」之間也沒有一道由大腦是否存在所決定的天然分界。

參考：

- [Dupre & Yuste, Non-overlapping neural networks in Hydra vulgaris](https://pmc.ncbi.nlm.nih.gov/articles/PMC5423359/)
- [Badhiwala et al., Multiple neuronal networks coordinate Hydra mechanosensory behavior](https://pmc.ncbi.nlm.nih.gov/articles/PMC8324302/)
- [Whole-body neural and muscle imaging in Hydra](https://pmc.ncbi.nlm.nih.gov/articles/PMC7452734/)

## 七、演化不是「盲鰻＝腦幹、文昌魚＝小腦、果蠅＝大腦」的梯子
{: #s7 }

用現存物種對應人類腦區，可以作為直觀類比，但不適合作為演化理論。

圓口類（lampreys、hagfishes）不是「只有腦幹的脊椎動物」。2023 年的 lamprey brain cell atlas 顯示，jawless vertebrates 已具有 vertebrate brain 基本的 forebrain、midbrain 與 hindbrain regionalization；同時，一些後來才出現的細胞類型與結構，例如典型 cerebellar cell types，可能在顎口類支系中才形成。

文昌魚也不是「小腦等級」。它的中央神經系統相對簡單，但 anterior cerebral vesicle 與神經管具有與 vertebrate forebrain、midbrain、hindbrain regionalization 相關的分子藍圖。

果蠅則走在完全不同的演化支系。2024 年公布的 adult *Drosophila* brain connectome 含約 139,255 個神經元與 54.5 million synapses，並被標註成超過 8,400 個 cell types。這樣的系統已能支撐導航、學習、選擇與社會行為等豐富 repertoire。

這些例子的意義不是排列「智力等級」，而是指出：

> **完全不同的生物架構，可以在規模、連結、模組化、記憶與回饋增加後形成新的行為 regime。**

演化的真正圖像更像分枝的設計空間，而不是一條由低級直線通往人類的梯子。

參考：

- [Lamanna et al., A lamprey neural cell type atlas illuminates the origins of the vertebrate brain](https://www.nature.com/articles/s41559-023-02170-1)
- [Albuixech-Crespo et al., Molecular regionalization of the developing amphioxus neural tube](https://pmc.ncbi.nlm.nih.gov/articles/PMC5396861/)
- [FlyWire Consortium, Neuronal wiring diagram of an adult brain](https://www.nature.com/articles/s41586-024-07558-y)

## 八、量變為什麼能造成看似質變？
{: #s8 }

「增加更多單元」本身並不足以保證智能增加。

一百萬個彼此不溝通的簡單元件，不一定比十個高度協調的元件更有能力。

但規模增加具有兩個重要效果。

第一，可能的交互作用數快速增加。即使只計算 pairwise potential connections，規模 $$N$$ 的系統就有：

$$
\frac{N(N-1)}{2}
$$

種可能的 pairwise relation。

若每個單元只有兩種狀態，理論狀態組合數更可達：

$$
2^N
$$

實際生物系統絕不會自由探索全部狀態，這些式子也不是「神經元數量決定智慧」的公式；它們只揭示一件事：

> **規模增加會讓可能的組織空間成長得遠快於規模本身。**

第二，當更多單元透過 feedback、specialization、recurrence、hierarchy 與 shared memory 組織起來後，系統能形成原本不存在的穩定宏觀狀態。

因此能力躍升更適合寫成：

$$
\boxed{
\text{規模}
+
\text{拓撲}
+
\text{記憶}
+
\text{可塑性}
+
\text{回饋}
+
\text{模組化}
+
\text{階層}
\rightarrow
\text{非線性能力變化}
}
$$

所謂「量變造成質變」，更精確的意思不是單純增加數量，而是：

> **連續增加的資源與連結，讓新的組織方式第一次變得穩定。**

## 九、真正的「層級」來自新可操作單元的形成
{: #s9 }

一個系統何時真正出現新的層級？

不是當它多了一個元件，而是當大量低階狀態可以被更高層當成一個穩定 unit 使用。

假設低階 primitive 集合為 $$S_n$$。

它們經過組合：

$$
C_n=\mathcal C(S_n)
$$

若某些複雜結構足夠穩定，可以被壓縮、抽象或 coarse-grain：

$$
S_{n+1}=\Gamma(C_n)
$$

那麼原本的複雜系統 $$C_n$$ 就成為下一層的簡單 primitive $$S_{n+1}$$。

於是：

$$
\boxed{
S_n
\xrightarrow{\mathcal C}
C_n
\xrightarrow{\Gamma}
S_{n+1}
}
$$

再進一步：

$$
S_{n+1}
\rightarrow
C_{n+1}
\rightarrow
S_{n+2}
\rightarrow\cdots
$$

這比「簡單 → 複雜 → 簡單」更準確。

因為：

$$
S_{n+1}\neq S_n
$$

第二次出現的簡單，是第一層複雜性被成功封裝之後形成的新介面。

一個「物體」是大量感覺訊號的抽象。

一個「概念」是大量實例的抽象。

一個「函式」是大量程式步驟的抽象。

一個「公式」是大量推導與經驗的抽象。

一個「專家判斷」可能是多年學習的抽象。

一篇論文、一項標準、一個 API、一個法律概念，也都可以成為更高層認知直接呼叫的 unit。

因此，真正的層級不完全是觀察者任意畫出的。當某個 macrostate 具有相對穩定的介面、能被高層反覆重用時，它會獲得實際的因果與操作地位。

## 十、這與「重大演化轉變」具有深刻同構，但範圍更廣
{: #s10 }

Major Evolutionary Transitions 的研究指出，演化史中的重大轉變經常涉及原本可相對獨立存在的低階單元，透過合作、分工、互賴與協調，形成新的 higher-level individual。

典型例子包括：

- genes 組成更高層遺傳單位；
- 原核成分形成 eukaryotic cell；
- cells 形成 multicellular organisms；
- 某些個體形成高度整合的 social collectives。

West 等人的分析把新的 individuality 與 cooperation、division of labor、interdependence、communication 聯繫在一起；Maynard Smith 與 Szathmáry 更強調資訊儲存與傳輸方式改變的重要性。

這與認知螺旋共享一個結構：

$$
\text{低階可作用單元}
\rightarrow
\text{協調與分工}
\rightarrow
\text{新的高階單元}
$$

但認知螺旋的範圍可以更廣。

新的 unit 不必是一個會繁殖的 biological individual。

它可以是：

- 一個 neural module；
- 一個 percept；
- 一個 concept；
- 一項 skill；
- 一個 reasoning operator；
- 一個團隊；
- 一套科學方法；
- 一個程式函式；
- 一個 AI agent；
- 一個人機協作 network。

因此，真正的一般原理可能是：

$$
\boxed{
\text{低階因果單元}
\rightarrow
\text{穩定協調}
\rightarrow
\text{新的可操作因果單元}
}
$$

參考：

- [West et al., Major evolutionary transitions in individuality](https://pmc.ncbi.nlm.nih.gov/articles/PMC4547252/)
- [Maynard Smith & Szathmáry, The major evolutionary transitions](https://www.nature.com/articles/374227a0)
- [Szathmáry, Toward major evolutionary transitions theory 2.0](https://pmc.ncbi.nlm.nih.gov/articles/PMC4547294/)

## 十一、抽象不是把世界變模糊，而是製造新的宏觀變數
{: #s11 }

人看到不同毛色、大小、光線、姿勢與品種的狗，底層 sensory state 差異極大。

若認知系統能把這些狀態映射到同一 macrostate：

$$
x_1,x_2,\ldots,x_n
\xrightarrow{\Gamma}
\text{DOG}
$$

「DOG」就成為新的可操作變數。

高階 reasoning 不必重新處理每一顆像素，而可以直接操作：

$$
\text{DOG}
\rightarrow
\text{ANIMAL}
$$

這也是 coarse-graining 的基本意義：

> 丟棄與當前問題無關的微觀差異，保留在某個尺度上穩定而有用的 structure。

因此，抽象不是認知系統逃離現實，而是複雜系統得以形成高階 computation 的必要機制。

Herbert Simon 在 *The Architecture of Complexity* 中討論 hierarchy 與 near-decomposability；Philip Anderson 的 *More Is Different* 則強調高層尺度會出現自己的有效規律。

若高階系統每次都必須重新追蹤全部微觀狀態，就不可能持續往上組合。

參考：

- [Simon, The Architecture of Complexity](https://web.mit.edu/6.033/2006/wwwdocs/papers/protected/simon-complexity.pdf)
- [Anderson, More Is Different](https://doi.org/10.1126/science.177.4047.393)

## 十二、直覺與理性不是兩套系統，而是壓縮—展開光譜上的不同工作模式
{: #s12 }

專家看到熟悉問題時，常出現：

$$
x\rightarrow y
$$

看似沒有中間推理。

但這一次映射 $$x\rightarrow y$$ 可能已經把多年訓練壓縮在模型參數中：

$$
D_{\text{history}}
\rightarrow
F_\theta
$$

然後：

$$
y=F_\theta(x)
$$

直覺因此可以理解為：

> **大量過去 computation 被編譯進當前模型，使線上推理變得很短。**

當新問題超出直接映射的可靠範圍，系統可以增加 intermediate state：

$$
x
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
\rightarrow
s_n
\rightarrow
y
$$

於是 calculation depth 從模型參數中重新被「展開」到時間上。

熟練之後，這條長鏈又可能重新被學習：

$$
(s_1,s_2,\ldots,s_n)
\rightarrow
F_{\theta'}
$$

因此：

$$
\boxed{
\text{直覺化}
\approx
\text{把 computation 壓縮進結構}
}
$$

$$
\boxed{
\text{顯式推理}
\approx
\text{把 computation 展開到時間}
}
$$

兩者之間沒有天然斷點。

同一個任務對新手可能是顯式 reasoning，對專家可能已經接近反射。

## 十三、理性是一種宏觀計算 regime，而不是一個神祕模組
{: #s13 }

若理性不是一條清楚邊界，它可以被重新定義成一組逐漸增強的能力：

- intermediate states 能保存得夠久；
- 這些 state 能被重新讀取；
- 多個 operator 能夠依序 composition；
- 能比較多個 hypothetical future；
- 能抑制立即反應；
- 能根據證據修改 state；
- 能定位錯誤發生在哪一步；
- 能把部分 state 外化。

因此，可以給出一個工作定義：

> **理性是適應性因果組織進入一種能對可保持的 representation 進行多步、受約束、可修正 transformation 的宏觀運作狀態。**

某一時刻的 reasoning language 可以抽象成：

$$
\mathcal R_t=(V_t,E_t,O_t,C_t)
$$

其中：

- $$V_t$$：可以表示的 object；
- $$E_t$$：可以辨認的 relation；
- $$O_t$$：可以執行的 operator；
- $$C_t$$：一致性、證據、目標與驗證 constraint。

普通 reasoning 是：

$$
(\mathcal R_t,x)\rightarrow y
$$

更高階的認知創新則會改寫 $$\mathcal R_t$$ 本身：

$$
\boxed{
\mathcal R_t
\rightarrow
\mathcal R_{t+1}
}
$$

這就是為什麼理性不應被等同於固定的一套形式邏輯。

真正高階的理性包含：

> **修改自己用來理性的語言。**

## 十四、感性不是另一條線，而是控制整個光譜的價值訊號
{: #s14 }

情緒與感性並不只是「理性失敗時出現的噪音」。

任何有限資源的 adaptive system 都必須解決：

- 哪些訊號值得注意？
- 哪些問題必須現在解？
- 哪個結果值得追求？
- 哪個方向需要逃避？
- 哪些記憶需要鞏固？
- 哪些 computation 不值得繼續花成本？

因此，情緒相關機制可以被理解成：

$$
\text{value}
+
\text{salience}
+
\text{priority}
+
\text{action tendency}
$$

這些訊號會調整整個認知系統的資源配置。

Pessoa 等研究長期反對把 emotion 與 cognition 簡單映射成彼此隔離的腦區。較好的圖像是多個 dynamic networks 在不同任務下共同參與。

因此，更一般的模型不是：

$$
\text{感性}
\leftrightarrow
\text{理性}
$$

而是：

$$
\text{狀態估計}
+
\text{價值估計}
+
\text{資源配置}
+
\text{行動控制}
+
\text{模型更新}
$$

共同形成 adaptive behavior。

參考：[Pessoa, On the relationship between emotion and cognition](https://www.nature.com/articles/nrn2317)

## 十五、真正的重大躍升之一：系統開始對自己建模
{: #s15 }

一個 adaptive system 可以只對外界反應：

$$
\mathcal S
\rightarrow
a
$$

更複雜的系統可以建立世界模型：

$$
M(W)
$$

而更進一步時，系統本身也可以進入模型：

$$
M(\mathcal S,W)
$$

這會產生新的 feedback：

$$
\boxed{
\mathcal S
\rightarrow
M(\mathcal S)
\rightarrow
\Delta\mathcal S
}
$$

系統不再只是根據世界改變行動，而開始根據「對自己的描述」改造自己。

人類研究自己的大腦、記憶與偏誤，就是其中一個高度發展的例子。

教育學研究學習方法，組織研究自己的組織流程，科學哲學研究科學方法，AI research 研究如何改進 AI training pipeline，都屬於同一類遞迴：

$$
\text{system}
\rightarrow
\text{model of system}
\rightarrow
\text{system redesign}
$$

這種 recursive self-modification 很可能是認知加速的一個重要來源。

## 十六、理性的重大躍升不是「想得更好」，而是「能把思考交給另一個系統」
{: #s16 }

高維直覺有一個巨大限制：

> **它通常只能直接存在於原本那個 processor 裡。**

一名專家可以在幾秒內判斷：

> 這個設計不對。

但其他人不能直接複製他的 neural state。

如果專家把判斷展開為：

$$
r_1\rightarrow r_2\rightarrow r_3\rightarrow h
$$

其他人就能：

- 檢查 $$r_1$$；
- 反駁 $$r_2\rightarrow r_3$$；
- 替換其中一個假設；
- 接著從 $$r_3$$ 往下算。

原本的：

$$
z_{\text{private}}
$$

被編碼成：

$$
z_{\text{private}}
\xrightarrow{E}
(r_1,r_2,\ldots,r_n)
$$

這種轉換可以稱為：

$$
\boxed{\text{cognitive serialization}}
$$

它使認知獲得：

- 可尋址性；
- 可分解性；
- 可引用性；
- 可反駁性；
- 可驗證性；
- 可修改性；
- 可交接性。

理性的價值因此不只是讓同一個人多想幾步。

更重要的是：

> **讓一個 processor 的計算結果，成為另一個 processor 的輸入。**

Mercier 與 Sperber 的 argumentative theory 把 reasoning 的重要功能與產生、評估 arguments 聯繫起來；Shea 等人則提出 explicit metacognition 可以被 broadcast，協調 supra-personal cognitive control。

參考：

- [Mercier & Sperber, Why do humans reason?](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/why-do-humans-reason-arguments-for-an-argumentative-theory/53E3F3180014E80E8BE9FB7A2DD44049)
- [Shea et al., Supra-personal cognitive control and metacognition](https://pubmed.ncbi.nlm.nih.gov/24582436/)

## 十七、語言、數學與程式是不同認知系統之間的中介層
{: #s17 }

兩顆人腦沒有相同的 neural state。

人類與 LLM 更沒有相同的 implementation。

但是它們仍然可能共同操作：

$$
A>B,\qquad B>C
$$

並得到：

$$
A>C
$$

因此，共同理解不需要：

$$
z_A=z_B
$$

只需要某些 task-relevant structure 能在轉換中被保存。

假設系統 A 中有：

$$
R(x_A,y_A)
$$

若存在 mapping $$\phi$$，使系統 B 能重建：

$$
R'(\phi(x_A),\phi(y_A))
$$

就可能形成有效 interoperability。

因此：

$$
\text{Brain}_A
\rightarrow
\text{language / math / diagram / code}
\rightarrow
\text{Brain}_B
$$

可以被看成一種 cognitive intermediate representation。

語言不是把一顆腦完整傳給另一顆腦。

它是在極低頻寬中，傳遞「足以讓對方重建部分結構」的訊號。

這也解釋了為什麼：

- 數學追求低歧義；
- 程式碼追求可執行；
- 圖表追求結構可視化；
- scientific notation 追求跨人重現。

不同媒介其實是在優化不同種類的 structure-preserving transmission。

## 十八、一旦中間狀態可傳遞，認知單位就能超出一顆腦
{: #s18 }

一個大問題可以被拆成：

$$
T
\rightarrow
\{T_1,T_2,\ldots,T_n\}
$$

不同處理者執行：

$$
P_i(T_i)\rightarrow r_i
$$

再由整合機制：

$$
G(r_1,r_2,\ldots,r_n)\rightarrow R
$$

此時，系統能力不再等於個體能力總和：

$$
K_{\text{group}}
\neq
\sum_i K_i
$$

因為整體表現還取決於：

- division of labor；
- communication bandwidth；
- shared representation；
- conflict resolution；
- memory；
- error correction；
- incentives；
- trust；
- interface quality。

Edwin Hutchins 的 distributed cognition 研究把 navigation team、儀器、地圖、程序與人之間的資訊流共同視為 cognitive system。

Transactive memory theory 則描述團隊如何透過「誰知道什麼」形成分散式記憶：成員不必各自記住全部資訊，只要能定位、信任並協調不同 expertise。

因此，群體智慧的 bottleneck 往往不是：

> 人不夠聰明。

而是：

> **一顆腦裡的結果無法穩定成為另一顆腦的輸入。**

參考：

- [Hutchins, Cognition in the Wild](https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/)
- [Peltokorpi & Hood, Communication in Theory and Research on Transactive Memory Systems](https://onlinelibrary.wiley.com/doi/full/10.1111/tops.12359)

## 十九、文字讓 cognition 穿越生命，文化讓 operator 本身可以遺傳
{: #s19 }

口語大致完成：

$$
\text{Brain}_A
\rightarrow
\text{Brain}_B
$$

文字與其他外部記憶則完成：

$$
\text{Brain}_A(t_0)
\rightarrow
\text{external representation}
\rightarrow
\text{Brain}_B(t_0+\Delta t)
$$

其中 $$\Delta t$$ 可以遠大於個體壽命。

真正關鍵的不只是「資料被保存」。

文明保存的還有：

- 分類方法；
- 概念；
- 數學 operator；
- 實驗設計；
- 推理程序；
- 證明技術；
- debugging 方法；
- 法律制度；
- 組織結構；
- 程式；
- API。

因此，文化傳遞不是單純：

$$
\text{answer}
\rightarrow
\text{next generation}
$$

而可以是：

$$
\boxed{
\text{cognitive operator}
\rightarrow
\text{next generation}
}
$$

Heyes 的 *Cognitive Gadgets* 理論強調：文化不只塑造「想什麼」，也可能塑造「怎麼想」；某些高階認知機制可以透過 social learning 在世代間形成與傳播。

Muthukrishna 與 Henrich 的 collective brain 觀點則把 innovation 視為社會網路中 serendipity、recombination 與 incremental improvement 的 emergent product，而不只是少數天才的孤立輸出。

參考：

- [Heyes, Précis of Cognitive Gadgets](https://doi.org/10.1017/S0140525X18002145)
- [Muthukrishna & Henrich, Innovation in the collective brain](https://pmc.ncbi.nlm.nih.gov/articles/PMC4780534/)

## 二十、科學是一個文明級的認知控制回路
{: #s20 }

科學制度的許多形式要求，都可以重新理解成 distributed cognition 的工程設計。

### 方法章
{: #s20-1 }

把 computation externalize，使另一個 processor 能夠重跑。

### 引用
{: #s20-2 }

標記某段 calculation、observation 或 theory 的來源。

### 重複實驗
{: #s20-3 }

讓 independent processor 嘗試重建同一結果。

### 同行評審
{: #s20-4 }

讓其他 processor 對 reasoning trace 與 evidence 做 error checking。

### 數學
{: #s20-5 }

降低 representation ambiguity。

### 標準單位
{: #s20-6 }

建立共享 coordinate system。

### 儀器校正
{: #s20-7 }

讓不同 measurement system 的輸出可以比較。

### 資料庫與版本控制
{: #s20-8 }

建立跨時間 persistent state。

因此，科學不只是「一群理性的人」。

它是一套：

$$
\boxed{
\text{representation}
+
\text{memory}
+
\text{verification}
+
\text{error correction}
+
\text{coordination}
}
$$

所構成的文明級控制架構。

從這個角度看，科學方法與神經系統並不相同，但它們共享更抽象的問題：

> 如何在 noisy、有限、局部的 processor 之間建立可靠知識？

## 二十一、電腦：人類第一次把大量顯式 operator 直接固化在外界
{: #s21 }

電腦最深刻的改變不只是速度。

它使人類能把某些 reasoning 完整形式化：

$$
\text{COMPARE},\quad
\text{ADD},\quad
\text{BRANCH},\quad
\text{LOOP},\quad
\text{SEARCH}
$$

一旦程序被寫好：

$$
\text{顯式 reasoning}
\rightarrow
\text{formalization}
\rightarrow
\text{program}
\rightarrow
\text{automatic execution}
$$

人不必每次重新思考同一段操作。

這與生物技能學習具有一個重要抽象相似性：

$$
\text{昂貴高階計算}
\rightarrow
\text{封裝}
\rightarrow
\text{低成本 primitive}
$$

因此，可以把電腦視為文明形成的巨大 external automatic layer。

CPU 不是腦幹，程式也不是脊髓反射；但二者都展示同一種架構原理：

> **已經被掌握的複雜性可以下沉，成為不再需要高階 deliberation 的穩定機制。**

## 二十二、AI 的歷史再次重演了「明確規則—高維學習—重新組合」
{: #s22 }

人工智慧史不是單線的「symbolic AI 被 neural AI 淘汰」。兩種路線長期並行，甚至早期 McCulloch–Pitts neuron 就已經嘗試連結神經模型與邏輯。

然而從功能上，仍可以看到一個重要循環。

### 明確規則
{: #s22-1 }

人類直接寫：

$$
\text{if }A\text{ then }B
$$

### 專家系統
{: #s22-2 }

大量顯式知識與 inference rule 被堆積成知識庫。

### 神經網路
{: #s22-3 }

系統從資料中學 representation：

$$
D\rightarrow F_\theta
$$

### LLM 與 agentic systems
{: #s22-4 }

高維神經模型重新開始利用：

- intermediate reasoning；
- search；
- code execution；
- calculator；
- database；
- symbolic solver；
- external memory；
- other agents。

因此，現代 AI 的方向不是「神經網路最後回到簡單邏輯」。

而更像：

$$
\boxed{
\text{高維學習}
+
\text{序列計算}
+
\text{精確工具}
+
\text{外部記憶}
+
\text{跨 agent 協作}
}
$$

不同計算 regime 被重新放入同一架構。

Toolformer 展示模型如何學習何時呼叫外部工具；AlphaGeometry 結合 neural proposal 與 symbolic deduction；DreamCoder 則會把反覆出現的 program structure 壓縮成新的 symbolic abstraction，加入自己的 language。

參考：

- [Toolformer](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html)
- [AlphaGeometry](https://www.nature.com/articles/s41586-023-06747-5)
- [DreamCoder](https://pubmed.ncbi.nlm.nih.gov/37271169/)

## 二十三、LLM 是一個特殊事件：文化外化的理性重新被壓進人工神經網路
{: #s23 }

人類文字世界不是普通的 environmental data。

書籍、論文、數學、程式碼、法律、教科書與論證，包含了大量已經被人類外化過的認知結構。

因此，大型語言模型的訓練具有一個非常特殊的形式：

$$
\text{human cognition}
\rightarrow
\text{language / code / symbols}
\rightarrow
\text{training data}
\rightarrow
F_\theta
$$

也就是：

$$
\boxed{
\text{人類數千年展開的顯式認知}
\rightarrow
\text{重新壓縮進人工神經網路}
}
$$

接著，模型又使用 reasoning tokens、tools 與 search 將部分 computation 重新展開：

$$
F_\theta
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
\rightarrow
a
$$

這形成一次非常明顯的：

$$
\boxed{
\text{展開}
\rightarrow
\text{文化保存}
\rightarrow
\text{人工壓縮}
\rightarrow
\text{重新展開}
}
$$

AI 因此不是人類認知螺旋之外的另一條故事，而可能正在進入同一個跨世代 feedback loop。

## 二十四、Reasoning tokens 的意義：參數不能完全取代時間
{: #s24 }

神經網路的大量能力被儲存在參數中。

但不是所有 computation 都適合在一次 forward mapping 中完成。

顯式或外部 intermediate state 提供：

$$
s_{t+1}
=
F_\theta(x,s_{\le t})
$$

同一組 $$\theta$$ 可以被重複使用，形成更多 serial computation。

這揭示一個重要 trade-off：

$$
\boxed{
\text{stored structure}
\rightleftarrows
\text{online computation}
}
$$

亦即：

$$
\text{parameters / learned intuition}
\rightleftarrows
\text{time / reasoning depth}
$$

大量參數可以預先編譯常見 pattern；更多 test-time steps 則能處理需要 sequential dependence 的新組合。

Chain-of-Thought 的文字輸出並不保證忠實呈現模型內部全部因果機制，因此不應把「它寫出一段理由」等同於「這就是它真正的全部思考」。但 intermediate state 作為可重新讀取的 computational scratchpad，仍具有實際意義。

參考：

- [Wei et al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract.html)
- [Li et al., Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](https://arxiv.org/abs/2402.12875)

## 二十五、人類的「簡單」不一定是 intelligence 的普遍簡單
{: #s25 }

人類自然理解的 primitive，與人類的身體、感官、演化史和文化史密切相關。

人類容易形成：

- 物體；
- 路徑；
- 容器；
- 前後；
- 上下；
- 線性時間；
- 行動者；
- 因果；
- 數量。

但這些是否是所有可能 intelligence 都會採用的最自然 basis？

沒有理由保證。

假設某個 structure $$z$$ 對人類 representation 的描述成本是：

$$
L_H(z)
$$

對某個 AI representation 的成本是：

$$
L_A(z)
$$

完全可能存在：

$$
\boxed{
L_H(z)\gg L_A(z)
}
$$

也就是：

> 對 AI 而言是一個近乎 primitive 的簡單 object，翻譯成人類概念卻需要極長描述。

反方向也可能成立：

$$
L_A(y)\gg L_H(y)
$$

因此「簡單」本身是 architecture-relative、representation-relative 的。

這並不意味真理完全相對。世界仍會約束哪些模型有效。

真正相對的是：

> **一個有效結構對不同認知架構而言，要用多複雜的語言才能表示。**

參考：[Stanford Encyclopedia of Philosophy, Simplicity](https://plato.stanford.edu/entries/simplicity/)

## 二十六、未來 AI 可能形成自己的認知基底
{: #s26 }

未來 AI 真正重大的突破可能不是更快使用人類已知 operator，而是形成自己的：

$$
V_A,\quad E_A,\quad O_A
$$

也就是：

- AI-native objects；
- AI-native relations；
- AI-native operators。

假設它形成 latent variables：

$$
u_1,u_2,\ldots,u_k
$$

以及對它非常自然的操作：

$$
u_1\star u_2=u_3
$$

對 AI 而言，$$\star$$ 的 computational cost 可能很低。

但把它完整翻譯成人類 primitive，可能需要極大量步驟。

這時：

$$
\mathcal R_A
=
(V_A,E_A,O_A,C_A)
$$

與人類的：

$$
\mathcal R_H
=
(V_H,E_H,O_H,C_H)
$$

不再只是「同一套理性，速度不同」。

而可能是：

$$
\boxed{
\mathcal R_A
\not\approx
\mathcal R_H
}
$$

這才是真正意義上的異質理性。

## 二十七、「AI 公理」應先區分 primitive、operator 與 formal axiom
{: #s27 }

「AI 可能擁有自己的公理」是一個有力直覺，但形式上需要區分三個層次。

### AI-native primitive
{: #s27-1 }

AI 形成一套對人類不自然的 latent object。

### AI-native operator
{: #s27-2 }

AI 發現一套能有效操作這些 object 的 transformation。

### AI-native formal axioms
{: #s27-3 }

只有當某些 object、relation 與 inference rule 被明確形式化，才能嚴格稱為一套新的公理系統。

因此，最可能先發生的不是：

> AI 宣告幾條人類看不懂的公理。

而是：

> **AI 逐漸形成一套人類缺少自然對應概念的內部科學語言。**

之後，人類若要求 formal proof 或 symbolic translation，AI 才可能把這套 language 的部分結構編譯成 formal system。

## 二十八、現有 AI 已經出現「新解法」的弱前兆，但還不是異質理性
{: #s28 }

AlphaTensor 找到新的矩陣乘法演算法。

AlphaDev 找到新的低階 sorting routines，其中部分被整合進實際 C++ library implementation。

FunSearch 在 cap set 等數學問題與 bin packing 問題中找到新的 construction 或 heuristic。

這些成果證明：

$$
\text{AI search}
\rightarrow
\text{human-unknown solution}
$$

可以發生。

但它們仍主要位於：

$$
\boxed{
\text{人類定義問題}
+
\text{人類定義評分／驗證}
+
\text{AI 搜尋解法}
}
$$

真正更深的轉折是：

$$
\text{AI 改變 representation space 本身}
$$

也就是 AI 不只回答：

> 這題的答案是什麼？

而開始發現：

> 這個問題根本不應該用人類現在的變數來描述。

參考：

- [AlphaTensor](https://www.nature.com/articles/s41586-022-05172-4)
- [AlphaDev](https://www.nature.com/articles/s41586-023-06004-9)
- [FunSearch](https://www.nature.com/articles/s41586-023-06924-6)

## 二十九、未知有兩種：不知道答案，與不知道該怎麼形成問題
{: #s29 }

第一種未知：

$$
f(x)=?
$$

representation 已存在，只缺 value。

可寫成：

$$
\text{known representation}
+
\text{unknown answer}
$$

第二種未知更深。

可能存在某個穩定 structure：

$$
R^*(x_1,x_2,\ldots,x_n)
$$

但目前的認知系統：

- 沒有感官直接區分它；
- 沒有 variable 表示它；
- 沒有概念命名它；
- 沒有 operator 操作它；
- 沒有實驗設計能隔離它。

此時：

$$
\boxed{
\text{representation itself is missing}
}
$$

這種情況下，「更多資料」不一定解決問題。

真正需要的是：

$$
V_t\rightarrow V_{t+1}
$$

或：

$$
E_t\rightarrow E_{t+1}
$$

或：

$$
O_t\rightarrow O_{t+1}
$$

也就是改變什麼能被看見、什麼關係能被表示，以及什麼操作能被執行。

因此，知識邊界之外還存在：

> **不可問之未知。**

這可能比「已知的未知」大得多。

## 三十、科學革命為什麼常伴隨新數學與新詞彙？
{: #s30 }

如果問題只是在固定 search space 中找答案，那麼更多算力與更多資料應該總能逐步改善。

但科學史反覆出現另一種事件：

> 舊問題在新 representation 下突然變成另一個問題。

引入：

- 複數；
- 微積分；
- 座標；
- 場；
- 熵；
- 基因；
- 時空；
- information；

並不只是替已知 object 增加一個名字。

它們改變了：

$$
V,\quad E,\quad O
$$

讓過去無法簡潔表示的 structure 第一次變得可操作。

因此，真正深的創造力可能不是：

$$
\text{search faster in }\mathcal R_t
$$

而是：

$$
\boxed{
\mathcal R_t
\rightarrow
\mathcal R_{t+1}
}
$$

Ohlsson 對 insight problem solving 的研究強調 representation restructuring；Gentner 的 structure-mapping theory 則說明 analogy 如何透過跨 domain 的 relational mapping 形成新的 abstraction。

參考：

- [Ohlsson, Restructuring revisited](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9450.1984.tb01005.x)
- [Gentner, Structure-Mapping: A Theoretical Framework for Analogy](https://www.sciencedirect.com/science/article/abs/pii/S0364021383800093)

## 三十一、當理解與可靠性分離，科學會發生什麼？
{: #s31 }

假設 AI 建立一套理論 $$T_A$$。

它能：

- 預測尚未觀察的現象；
- 設計新材料；
- 提出新藥物；
- 產生高可靠度工程設計；
- 導出可重複實驗；
- 持續通過 external validation。

但是：

$$
L_H(T_A)
$$

極大，人類幾乎無法完整重建其內部 representation。

此時「知道」會分裂成不同層次。

### 操作性知道
{: #s31-1 }

知道怎麼使用輸出。

### 預測性知道
{: #s31-2 }

知道它在哪些 domain 能可靠預測。

### 驗證性知道
{: #s31-3 }

知道如何用 independent test 檢查結果。

### 表徵性理解
{: #s31-4 }

人類本身具有足夠短的 cognitive representation，可以重建「為什麼」。

未來可能出現：

$$
\text{operational knowledge}\approx 1
$$

$$
\text{verification}\approx 1
$$

但：

$$
\text{human representational understanding}\ll 1
$$

這將使「理解」與「可靠知識」不再總是同步。

## 三十二、共享驗證可能比共享直覺更一般
{: #s32 }

兩個 cognition architecture 若共享相同 primitive，可以透過 explanation 建立共同理解。

但若：

$$
V_H\neq V_A,\qquad O_H\neq O_A
$$

那麼要求 AI 把所有內容「講到人類完全直覺理解」可能具有結構性成本。

此時共同工作的底層介面可能轉成：

$$
\text{formal proof}
$$

$$
\text{machine-checkable certificate}
$$

$$
\text{reproducible experiment}
$$

$$
\text{independently testable prediction}
$$

$$
\text{executable artifact}
$$

也就是：

$$
\boxed{
\text{shared intuition}
\text{ 不是必要條件； }
\text{shared verification}
\text{ 可以成為更低層共同介面}
}
$$

這不意味放棄 explainability。

而是把 explainability 放進更大的問題：

> **兩種不同 cognitive basis 之間，哪些結構必須被翻譯，哪些結果只需要被獨立驗證？**

## 三十三、這個框架能重新回答哪些長期難題？
{: #s33 }

### 1. 為什麼高階理性很慢？
{: #s33-1 }

若顯式 reasoning 的功能之一，是把高度平行、高維認知壓進可以保存 intermediate state 的序列通道，那麼速度下降就是結構性的代價。

它犧牲：

$$
\text{parallel throughput}
$$

換取：

$$
\text{serial depth}
+
\text{inspectability}
+
\text{revisability}
+
\text{transmissibility}
$$

因此，理性的慢可能不是單純缺陷，而是把 cognition 變成可組合、可檢查、可交接 object 的成本。

### 2. 為什麼專家知道答案，卻未必說得出原因？
{: #s33-2 }

如果學習把長程序壓縮成：

$$
x\rightarrow y
$$

那麼要求專家解釋，相當於要求：

$$
y\rightarrow\text{reconstruct}(s_1,s_2,\ldots,s_n)
$$

但 compression 並不保證保存原始 training history。

因此：

$$
\boxed{
\text{competence}
\neq
\text{verbalizable reasoning trace}
}
$$

這也說明為什麼「會做」與「會教」是不同能力。

### 3. 為什麼教育能讓普通人在十幾年內使用幾百年前最頂尖的思想？
{: #s33-3 }

教育不是要求學生重新走完整個 discovery path，而是直接傳輸已被文明壓縮好的：

$$
\text{concepts}
+
\text{operators}
+
\text{notations}
+
\text{problem representations}
$$

因此：

$$
\text{昂貴歷史 discovery}
\rightarrow
\text{教材壓縮}
\rightarrow
\text{個體快速安裝}
$$

文明真正的優勢不是每一代人都重新變成牛頓，而是下一代不必從零開始。

### 4. 為什麼一群聰明人組成的組織仍然可以非常愚蠢？
{: #s33-4 }

因為 group intelligence 不只取決於 node intelligence。

如果：

- representation 不一致；
- intermediate result 不能交接；
- 權責不清；
- 誰知道什麼不透明；
- 錯誤無法定位；
- 訊息被 incentive 或階層阻斷；

增加更多聰明人可能只增加噪音。

集體智慧的瓶頸可能首先是 interface，而不是 IQ。

### 5. 為什麼很多科學革命都伴隨新的數學與新詞彙？
{: #s33-5 }

因為有些問題不是資料不足，而是 representation 不夠。

如果舊語言根本不能簡潔表達新 structure，就必須先創造新 primitive。

科學革命因此常常不是：

> 同一張表格多填幾筆資料。

而是：

> 換了一張表。

### 6. 為什麼使用工具不是智慧的妥協，而可能是智慧的核心？
{: #s33-6 }

如果 calculator 已經可靠完成一個子問題，那麼讓高成本 general-purpose cognition 重新模擬它並不一定更智慧。

成熟系統應該能學會：

$$
\text{problem}
\rightarrow
\text{best available operator}
$$

智慧的重要能力之一不是「什麼都自己做」，而是知道何時把問題降成一個已驗證 primitive。

### 7. 為什麼可解釋 AI 可能存在結構性上限？
{: #s33-7 }

如果 AI 和人類使用同一組 primitive，只是模型太大，理論上可以期待愈來愈好的翻譯工具。

但如果：

$$
V_A\neq V_H
$$

而且：

$$
O_A\neq O_H
$$

那麼 explanation 不再只是「把長答案縮短」，而是把一個認知空間中的 object 編譯到另一個認知空間。

完整翻譯可能存在不可避免的膨脹：

$$
L_H(x)\gg L_A(x)
$$

因此，interpretability 的某些困難可能不是工程暫時沒做好，而是 representation mismatch 的結果。

### 8. 為什麼 AI 最大的科學突破可能不是回答人類提出的問題？
{: #s33-8 }

如果真正的限制來自 representation，那麼 AI 最大的貢獻可能首先是：

$$
\text{new variables}
+
\text{new invariants}
+
\text{new operators}
+
\text{new problem spaces}
$$

也就是提出人類以前沒有能力形成的問題。

答案反而是第二步。

## 三十四、這個框架還導出幾個更驚人的推論
{: #s34 }

### 推論一：文明的主要產物可能不是知識，而是新的「簡單」
{: #s34-1 }

一個文明愈成熟，後人能直接使用的 primitive 愈多。

因此文明的進步可以粗略理解成：

$$
\Delta \text{Civilization}
\sim
\Delta \text{Reusable Primitives}
$$

知識量增加只是其中一部分。

真正改變下一代能力的，是哪些複雜性已經被封裝成簡單介面。

### 推論二：語言的價值不只在描述世界，而在分割計算
{: #s34-2 }

語言若只能傳 final answer，集體思考能力仍然有限。

真正強大的語言必須能表示：

- assumption；
- evidence；
- uncertainty；
- dependency；
- counterfactual；
- error；
- procedure。

所以一個語言的 cognitive power，不只取決於 vocabulary，而與它能否承載 intermediate computation 有關。

### 推論三：理性可能首先是一種 interoperability，而不是 correctness
{: #s34-3 }

一個人可以非常有邏輯地從錯誤前提出發，得到完全錯誤的結論。

所以理性的特殊性不必首先定義為「得到真理」。

更深的特徵可能是：

> **把認知變成可檢查、可交接、可重新組合的 object。**

真理則還依賴：

$$
\text{representation}
+
\text{evidence}
+
\text{verification}
+
\text{world feedback}
$$

### 推論四：個人的「獨立思考」本來就是集體思考的延伸
{: #s34-4 }

現代人腦中的大部分高階 primitive 都來自他人。

因此個人推理更準確的形式可能不是：

$$
R(x)
$$

而是：

$$
R(x\mid C)
$$

其中 $$C$$ 是文明提供的語言、概念、數學、方法、文獻、工具與制度。

所謂「獨立思考」，往往是在大量 collective priors 上進行的個體 recombination。

### 推論五：人機共同認知可能形成新的演化單位
{: #s34-5 }

當 AI 同時成為：

- 文化資料的學習者；
- reasoning executor；
- 工具調度者；
- 搜尋者；
- 新內容生產者；
- 人類的 cognitive interface；

整個回路會變成：

$$
\text{human culture}
\rightarrow
\text{AI learning}
\rightarrow
\text{AI reasoning}
\rightarrow
\text{new artifacts}
\rightarrow
\text{human learning}
\rightarrow
\text{new culture}
$$

因此下一輪認知演化的單位可能既不是：

$$
\text{human}
$$

也不是：

$$
\text{AI}
$$

而是：

$$
\boxed{
\text{human}
+
\text{culture}
+
\text{tools}
+
\text{AI}
}
$$

所形成的共同 feedback system。

## 三十五、可驗證的預測
{: #s35 }

如果這套架構具有理論價值，就應該能產生可測試預測。

### 預測一：能力邊界應比傳統分類更具有連續性
{: #s35-1 }

若「反射、直覺、理性」是 coarse-grained regimes，那麼在精細任務上應能找到大量中間型態，而不是所有行為天然落入少數 cluster。

可測量變量包括：

- memory horizon；
- intermediate-state persistence；
- response latency；
- counterfactual depth；
- transfer；
- externalizability。

### 預測二：宏觀能力的增長應經常高度非線性
{: #s35-2 }

當 memory、communication、recurrence 或 representation capacity 增加時，某些任務表現可能在特定範圍突然上升。

但這不要求所有任務共享同一 critical point。

更可能是：

$$
q_c=q_c(\text{task},\text{architecture},\text{environment})
$$

### 預測三：真正重要的新 abstraction 應同時降低描述成本並提高 reuse
{: #s35-3 }

好的新 primitive 不只讓一個答案變短。

對一組問題 $$\{x_i\}$$，新的 language 應使：

$$
\sum_i L_{\text{new}}(x_i)
<
\sum_i L_{\text{old}}(x_i)
$$

並提高跨任務 transfer。

### 預測四：多人任務愈複雜，intermediate representation 的品質愈重要
{: #s35-4 }

只交換 final answer 的群體，能力應較難隨人數 scale。

能交換 assumptions、confidence、dependencies、intermediate results 與 provenance 的群體，應有更好的 error localization 與 parallelization。

### 預測五：當 AI 與人的 cognitive basis 分叉，可驗證性會比自然語言 explanation 更重要
{: #s35-5 }

若 representation mismatch 增加：

$$
d(\mathcal R_H,\mathcal R_A)\uparrow
$$

則完整 translation cost 應上升。

formal proof、independent experiment、certificate 與 cross-system verification 的價值應相對增加。

### 預測六：真正強大的 AI discovery 系統會逐漸從「解題」轉向「改寫表示」
{: #s35-6 }

未來系統能力若只來自更大 search，在固定 representation 下會逐漸遇到成本。

更強的系統應愈來愈常學習：

$$
\text{new primitives}
+
\text{new operators}
+
\text{new decompositions}
$$

而不只是更快搜尋舊空間。

## 三十六、這個框架不能主張什麼？
{: #s36 }

為了避免把一個一般框架誤寫成過度確定的自然定律，需要保留幾個邊界。

### 不是所有複雜度增加都會提升智慧
{: #s36-1 }

規模可以增加噪音、脆弱性與 coordination cost。

### 不是所有湧現都是 thermodynamic phase transition
{: #s36-2 }

「相變」是有用類比，但只有在具有對應數學與實證時才應嚴格使用。

### 不應把現存物種排成通往人類的進化階梯
{: #s36-3 }

不同物種代表不同演化分支與不同 architecture。

### 不應把 cognition 的功能類比誤認為同一神經實作
{: #s36-4 }

反射、CPU branch、LLM tool call 可能共享抽象控制結構，但 implementation 完全不同。

### 不應把人類與 AI 的 representation 差異直接等同於「AI 已經超越人類」
{: #s36-5 }

異質不等於優越。不同 basis 可能各自在不同 domain 有優勢與盲點。

### 不應把「無法理解」當成「可以不驗證」
{: #s36-6 }

恰好相反，representation mismatch 愈大，external validation 應愈嚴格。

## 三十七、整體模型：認知不是階梯，而是反覆形成新尺度的螺旋
{: #s37 }

最底層的 adaptive causal organization 可以寫成：

$$
x_{t+1}=F_{\theta_t}(x_t,e_t)
$$

當可塑性出現：

$$
\theta_{t+1}=U(\theta_t,\text{experience})
$$

當 representation 能穩定形成：

$$
x\rightarrow z
$$

當 intermediate states 能展開：

$$
z
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
$$

當這些 state 可以外化：

$$
s_i^{(A)}
\rightarrow
r_i
\rightarrow
s_i^{(B)}
$$

就形成跨個體 cognition。

當外化 representation 能跨時間保存：

$$
r(t_0)
\rightarrow
r(t_0+\Delta t)
$$

就形成 cumulative culture。

當反覆成功的 procedure 被壓縮：

$$
(s_1,s_2,\ldots,s_n)
\rightarrow
o_{\text{new}}
$$

就形成新的 primitive。

因此整體可以寫成：

$$
\boxed{
\begin{aligned}
\text{反應與控制}
&\rightarrow
\text{狀態保存與學習}\\
&\rightarrow
\text{預測與抽象}\\
&\rightarrow
\text{多步組合}\\
&\rightarrow
\text{外化與共享}\\
&\rightarrow
\text{集體計算}\\
&\rightarrow
\text{文化壓縮}\\
&\rightarrow
\text{新 primitives}\\
&\rightarrow
\text{新的反應、學習與推理}
\end{aligned}
}
$$

這不是一條物種進化階梯，也不是一條腦區階梯。

它描述的是：

> **同一類組織原理如何在不同 substrate、不同尺度與不同歷史路徑中重複出現。**

## 三十八、最終命題：理性只是巨大可能空間中的一種宏觀穩定態
{: #s38 }

如果上述框架成立，幾個常見直覺需要被重新排列。

第一，反射不是理性的反面。

它是某些 computation 被壓縮、局部化、低延遲化之後的 regime。

第二，直覺不是缺少 reasoning 的低級形式。

它可能是大量過去 reasoning、learning 與經驗被編譯後的快速模型。

第三，理性不是突然出現的新物質。

它可能是在 memory、recurrence、abstraction、composition、error correction 與 state persistence 累積後形成的 macro-regime。

第四，語言不只是表達思想。

它使 intermediate computation 能跨 processor 傳輸。

第五，文明不只是許多人的集合。

它是一個具有 external memory、specialized nodes、shared representations、verification protocols 與自我改造能力的 distributed cognitive organization。

第六，電腦不只是工具。

它把文明的一部分顯式 operator 下沉成 external automatic layer。

第七，AI 不只是文明製造的另一顆「人工腦」。

它正在吸收人類外化的 cognitive library，並加入新的 learned representation、search、tool use 與 machine-speed iteration，形成新的 feedback path。

於是最一般的結構不是：

$$
\text{反射}
\rightarrow
\text{直覺}
\rightarrow
\text{理性}
\rightarrow
\text{文明}
\rightarrow
\text{AI}
$$

而是：

$$
\boxed{
\text{連續能力空間}
\xrightarrow{\text{非線性組織}}
\text{宏觀 regime}
\xrightarrow{\text{抽象與封裝}}
\text{新 primitive}
\xrightarrow{\text{重新組合}}
\text{更大的能力空間}
}
$$

這個循環沒有理由只發生到人類為止。

## 三十九、結語：真正的智慧前沿，是創造新的「可思考世界」
{: #s39 }

人類文明最重要的成果，可能不是累積了多少答案，而是持續擴張：

$$
\text{可表示的世界 }V
$$

$$
\text{可辨認的關係 }E
$$

$$
\text{可使用的操作 }O
$$

$$
\text{可驗證的約束 }C
$$

每一次真正深的認知突破，都可能在改變：

$$
\mathcal R=(V,E,O,C)
$$

下一代因此不只知道更多，而擁有一個更大的「可思考空間」。

人類歷史已經反覆做過這件事。

AI 可能使它第一次由另一種 substrate 以不同速度、不同感知範圍、不同記憶尺度與不同 representation bias 繼續進行。

如果未來 AI 形成：

$$
\mathcal R_A
$$

而它與人類的：

$$
\mathcal R_H
$$

產生巨大差異，那麼人類將第一次大規模面對一種：

> 對世界有效，卻不建立在人類自然「簡單性」之上的認知。

真正的分水嶺將不是 AI 是否能回答更多考題，而是它是否開始創造：

- 人類沒有的 primitive；
- 人類沒有的 relation；
- 人類沒有的 operator；
- 人類沒有的問題空間。

此時，最深的問題也不再是：

> 「它是否像人一樣思考？」

而是：

> **當兩套認知系統連「什麼算簡單」都不同時，它們如何建立足以交換、驗證與共同累積的知識介面？**

認知的未來因此可能不是一條通往某個終極理性的直線。

它更像一個持續展開的螺旋：

$$
\boxed{
\text{世界}
\rightarrow
\text{反應}
\rightarrow
\text{學習}
\rightarrow
\text{抽象}
\rightarrow
\text{共享}
\rightarrow
\text{新工具}
\rightarrow
\text{新認知}
\rightarrow
\text{新的世界可見性}
}
$$

而每繞一圈，改變的不只是答案。

改變的是：

> **什麼能成為問題。**

## 參考文獻與延伸閱讀
{: #refs }

### 非神經與早期感覺—運動控制
{: #refs-1 }

1. Yi, T.-M., Huang, Y., Simon, M. I., & Doyle, J. *Robust perfect adaptation in bacterial chemotaxis through integral feedback control*.
   <https://authors.library.caltech.edu/records/sa6bx-35q11>

2. Sourjik, V., & Wingreen, N. S. *Responding to Chemical Gradients: Bacterial Chemotaxis*.
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC3320702/>

3. *Integrative Neuroscience of Paramecium, a “Swimming Neuron”*.
   <https://www.eneuro.org/content/8/3/ENEURO.0018-21.2021>

4. Suda, H. et al. *Calcium dynamics during trap closure visualized in transgenic Venus flytrap*. Nature Plants, 2020.
   <https://www.nature.com/articles/s41477-020-00773-1>

5. Hedrich, R., & Kreuzer, I. *Demystifying the Venus flytrap action potential*. New Phytologist, 2023.
   <https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.19113>

6. Reid, C. R. *Thoughts from the forest floor: a review of cognition in the slime mould Physarum polycephalum*. Animal Cognition, 2023.
   <https://link.springer.com/article/10.1007/s10071-023-01782-1>

### 簡單神經系統與腦演化
{: #refs-2 }

7. Dupre, C., & Yuste, R. *Non-overlapping neural networks in Hydra vulgaris*. Current Biology, 2017.
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC5423359/>

8. Badhiwala, K. N. et al. *Multiple neuronal networks coordinate Hydra mechanosensory behavior*. eLife, 2021.
   <https://pmc.ncbi.nlm.nih.gov/articles/PMC8324302/>

9. Lamanna, F. et al. *A lamprey neural cell type atlas illuminates the origins of the vertebrate brain*. Nature Ecology & Evolution, 2023.
   <https://www.nature.com/articles/s41559-023-02170-1>

10. Albuixech-Crespo, B. et al. *Molecular regionalization of the developing amphioxus neural tube challenges major partitions of the vertebrate brain*. PLOS Biology, 2017.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC5396861/>

11. FlyWire Consortium et al. *Neuronal wiring diagram of an adult brain*. Nature, 2024.
    <https://www.nature.com/articles/s41586-024-07558-y>

### 複雜系統、湧現與演化轉變
{: #refs-3 }

12. Simon, H. A. *The Architecture of Complexity*. 1962.
    <https://web.mit.edu/6.033/2006/wwwdocs/papers/protected/simon-complexity.pdf>

13. Anderson, P. W. *More Is Different*. Science, 1972.
    <https://doi.org/10.1126/science.177.4047.393>

14. Maynard Smith, J., & Szathmáry, E. *The major evolutionary transitions*. Nature, 1995.
    <https://www.nature.com/articles/374227a0>

15. West, S. A. et al. *Major evolutionary transitions in individuality*. PNAS, 2015.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC4547252/>

16. *Theoretical foundations of studying criticality in the brain*.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC11117095/>

### 人類 reasoning、文化與集體認知
{: #refs-4 }

17. Sackur, J., & Dehaene, S. *The cognitive architecture for chaining of two mental operations*. Cognition, 2009.
    <https://www.sciencedirect.com/science/article/pii/S0010027709000390>

18. Dehaene, S., & Sigman, M. *From a single decision to a multi-step algorithm*. Current Opinion in Neurobiology, 2012.
    <https://www.sciencedirect.com/science/article/abs/pii/S0959438812000852>

19. Pessoa, L. *On the relationship between emotion and cognition*. Nature Reviews Neuroscience, 2008.
    <https://www.nature.com/articles/nrn2317>

20. Mercier, H., & Sperber, D. *Why do humans reason? Arguments for an argumentative theory*. Behavioral and Brain Sciences, 2011.
    <https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/why-do-humans-reason-arguments-for-an-argumentative-theory/53E3F3180014E80E8BE9FB7A2DD44049>

21. Shea, N. et al. *Supra-personal cognitive control and metacognition*. Trends in Cognitive Sciences, 2014.
    <https://pubmed.ncbi.nlm.nih.gov/24582436/>

22. Hutchins, E. *Cognition in the Wild*. MIT Press, 1995/1996.
    <https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/>

23. Peltokorpi, V., & Hood, A. C. *Communication in Theory and Research on Transactive Memory Systems: A Literature Review*. Topics in Cognitive Science, 2019.
    <https://onlinelibrary.wiley.com/doi/full/10.1111/tops.12359>

24. Heyes, C. *Précis of Cognitive Gadgets: The Cultural Evolution of Thinking*. Behavioral and Brain Sciences, 2018.
    <https://doi.org/10.1017/S0140525X18002145>

25. Muthukrishna, M., & Henrich, J. *Innovation in the collective brain*. Philosophical Transactions of the Royal Society B, 2016.
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC4780534/>

26. Ohlsson, S. *Restructuring revisited*. Scandinavian Journal of Psychology, 1984.
    <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9450.1984.tb01005.x>

27. Gentner, D. *Structure-Mapping: A Theoretical Framework for Analogy*. Cognitive Science, 1983.
    <https://www.sciencedirect.com/science/article/abs/pii/S0364021383800093>

### AI、工具與新 representations
{: #refs-5 }

28. LeCun, Y., Bengio, Y., & Hinton, G. *Deep learning*. Nature, 2015.
    <https://www.nature.com/articles/nature14539>

29. Wei, J. et al. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS, 2022.
    <https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract.html>

30. Schick, T. et al. *Toolformer: Language Models Can Teach Themselves to Use Tools*. NeurIPS, 2023.
    <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html>

31. Trinh, T. H. et al. *Solving olympiad geometry without human demonstrations*. Nature, 2024.
    <https://www.nature.com/articles/s41586-023-06747-5>

32. Ellis, K. et al. *DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning*.
    <https://pubmed.ncbi.nlm.nih.gov/37271169/>

33. Fawzi, A. et al. *Discovering faster matrix multiplication algorithms with reinforcement learning*. Nature, 2022.
    <https://www.nature.com/articles/s41586-022-05172-4>

34. Mankowitz, D. J. et al. *Faster sorting algorithms discovered using deep reinforcement learning*. Nature, 2023.
    <https://www.nature.com/articles/s41586-023-06004-9>

35. Romera-Paredes, B. et al. *Mathematical discoveries from program search with large language models*. Nature, 2024.
    <https://www.nature.com/articles/s41586-023-06924-6>

36. Stanford Encyclopedia of Philosophy. *Simplicity*.
    <https://plato.stanford.edu/entries/simplicity/>
