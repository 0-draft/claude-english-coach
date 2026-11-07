# Duolingo 系アプリから何を取り入れたか

2026-11 時点で、Duolingo と類似アプリ (Speak、Babbel、ELSA、Anki など) について、続けさせる仕組みと英語力が伸びる仕組みを調べ、English Rounds (`app/rounds.html`) に何を入れたかをまとめた。Duolingo の数字の多くは社内の A/B テストで、数億人規模で +0.4〜3% の差なので、1 人で使うときの効果は目安でしかない。

## 取り入れたもの

| 機能 | 根拠 | 証拠の強さ |
| --- | --- | --- |
| 連続 (ストリーク) は 5 分か復習を全部で延びる。ゴールの 15 分とは分ける | 連続の条件を日々のゴールから切り離したら、14 日後の継続率が +3.3%、連続中の学習者が +10.5% ([Duolingo 2020](https://blog.duolingo.com/improving-the-streak)) | 中 (社内 A/B) |
| 休みは 7 日に 1 回まで連続が切れない | Streak Freeze で DAU +0.38% ([Duolingo 2022](https://blog.duolingo.com/how-duolingo-streak-builds-habit))。1 日休んでも習慣化への影響は小さい (Lally 2010) | 中、効果は小 |
| 節目 (3、7、14、30、66 日) で一言出す | マイルストーンの演出で、新規の 7 日後の残存が +1.7% (同上) | 中 |
| AI と仕事の場面で会話し、話した語数を記録する | 日本人の英語学習者を対象にした Video Call の RCT で、話す力の伸びを一番よく予測したのは 1 回の会話でしゃべった語数 ([Duolingo 2025](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_video_call_improves_speaking_2025.pdf)) | 中 (社内 RCT、効果量は未確認) |
| 間違えたら、まず場所だけ示してもう一度直させる。それでもダメなら答えと「なぜ?」の解説を出す | 自分で直させる訂正 (prompt) は、言い直して見せる訂正 (recast) より効く ([Lyster & Saito 2010](https://www.researchgate.net/publication/234580927_Oral_Feedback_in_Classroom_SLA_A_Meta-Analysis)) | 強 (メタ分析) |
| ディクテーションの速さを、正答率が 80〜90% に収まるように自動で上げ下げする | Duolingo の Birdbrain は正答確率を予測して難しさを合わせる ([Duolingo 2020](https://blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain))。最適な正答率は約 85% という理論 ([Wilson et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6831579/)) | 弱〜中 |
| 月に 1 回、同じ条件で聞き取りと 2 分スピーチを測る | Duolingo の効果研究は読む・聞くに偏っていて、XP は稼ぎ目的の練習を生む ([Jiang et al. 2021](https://doi.org/10.1111/flan.12600), [arXiv 2203.16175](https://arxiv.org/pdf/2203.16175))。進み具合は実力で測る | 推論 |
| 毎朝のリマインドの文面を日替わりにする | 新しい文面ほど通知が効く ([Yancey & Settles 2020](https://research.duolingo.com/papers/yancey.kdd20.pdf)) | 強め、効果は小 |

## 取り入れなかったもの

- **リーグ、フレンド、フレンドクエスト**: 比べる相手がいないと成り立たない
- **ハート、エナジー**: 間違いに罰を与えると挑戦しなくなる。Duolingo 自身もハートをやめてエナジーに変えた
- **宝箱、ジェム、XP ブースト**: 簡単な問題を繰り返して稼ぐ行動を招く。ゲーム要素の行動面への効果は小さく安定しない ([Sailer & Homner 2020](https://doi.org/10.1007/s10648-019-09498-w))
- **パーフェクトレッスン**: 効果のデータが見つからない。完璧を狙って難しい問題を避けるようになるおそれがある
- **発音の自動採点 (ELSA 型)**: Artifact ではマイクが使えない

## Duolingo そのものの評価

- 読む・聞く力は伸びるが、聞く力は読む力より遅れる (Jiang et al. 2021、スポンサー研究、事前テストなし)
- 話す力の伸びは、文法や語彙より弱い ([Loewen et al. 2019](https://www.researchgate.net/publication/333431833_Mobile-assisted_language_learning_A_Duolingo_case_study))。Babbel と比べても差はなく、どちらも単体では高いレベルに届かない ([Kessler et al. 2023](https://doi.org/10.1080/09588221.2023.2215294))
- 「34 時間で大学 1 学期分」という有名な数字は、選択式テストと「授業なし」の比較で、会話力は測っていない ([Krashen の批判](http://sdkrashen.com/content/articles/krashen-does-duolingo-trump.pdf))
- Speak、Praktika、Loora の AI 会話アプリは、公開された効果研究が見つからなかった
