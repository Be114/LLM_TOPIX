# LLM TOPIX

> LLM および生成AI ニュースの包括的なWebプラットフォーム。主要なLLMプロバイダー（Gemini、ChatGPT、Claude）からの分析と洞察を提供します。

[![Built with TDD](https://img.shields.io/badge/Built%20with-TDD-green.svg)](https://en.wikipedia.org/wiki/Test-driven_development)
[![Code Coverage](https://img.shields.io/badge/Coverage-90%25+-brightgreen.svg)](#testing)
[![Performance](https://img.shields.io/badge/API%20Response-<50ms-blue.svg)](#performance-requirements)
[![Accessibility](https://img.shields.io/badge/WCAG-2.1%20AA-blue.svg)](#accessibility)

## 🎯 プロジェクト概要

LLM TOPIX は、LLMおよび生成AIニュースの決定版となるように設計されており、エンタープライズグレードのアーキテクチャと厳格なテスト駆動開発の原則で構築されています。私たちのプラットフォームは、パフォーマンス、アクセシビリティ、セキュリティをコアとして、厳選されたコンテンツを提供します。

### 主な機能

#### 🚀 フェーズ1（現在 - MVP）
- ✅ **最新記事表示**: 最新5件のLLMニュース記事を紹介するホームページ
- ✅ **レスポンシブ記事カード**: タイトル、要約（100文字）、公開日、ソースを含むクリーンでアクセシブルなカード
- ✅ **パフォーマンス最適化**: 50ms未満のAPIレスポンスと16ms未満のフロントエンドインタラクション
- ✅ **アクセシビリティファースト**: WCAG 2.1 AA準拠、キーボードナビゲーションとスクリーンリーダーサポート
- ✅ **RESTful API**: 標準化されたレスポンス形式による堅牢なエラーハンドリング
- ✅ **完全なTDD実装**: RED → GREEN → REFACTOR手法による包括的なテストカバレッジ

#### 🔮 フェーズ2（計画中）
- [ ] **高度な検索とフィルタリング**: 複数のフィルタ条件によるコンテンツ発見
- [ ] **ユーザー認証**: パーソナライズされた設定と閲覧履歴
- [ ] **LLM文書分析**: AI駆動の要約と洞察
- [ ] **リアルタイム更新**: プッシュ通知付きライブニュースフィード
- [ ] **コンテンツ管理システム**: コンテンツキュレーション用管理インターフェース

## 🛠 技術スタック

### フロントエンドアーキテクチャ
- **フレームワーク**: TypeScript（ストリクトモード）付きNext.js 14+
- **UIライブラリ**: 関数コンポーネントとhooks付きReact 18+
- **スタイリング**: パフォーマンス最適化されたCSS Modules
- **型安全性**: ブランド型と包括的なTypeScriptインターフェース
- **テスト**: React Testing Library付きJest
- **パフォーマンス**: React.memo、useMemo、コンポーネント最適化

### バックエンドアーキテクチャ
- **フレームワーク**: SQLAlchemy ORM付きPython Flask
- **言語**: 包括的な型ヒント付きPython 3.11+
- **データベース**: 最適化されたインデックス付きPostgreSQL 15+
- **API設計**: 標準化されたエラーレスポンス付きRESTfulエンドポイント
- **パフォーマンス監視**: 組み込み実行時間追跡
- **テスト**: 90%以上のカバレッジ要件付きPyTest

### 開発・運用
- **コンテナ化**: マルチサービスdocker-compose設定付きDocker
- **依存関係管理**: Poetry（Python）、npm（Node.js）
- **コード品質**: Black、Flake8、MyPy（Python）; ESLint、Prettier（TypeScript）
- **バージョン管理**: Conventional Commits仕様付きGit
- **CI/CD**: 自動テストとデプロイメント付きGitHub Actions

## 🚀 クイックスタート

### 前提条件

以下がインストールされていることを確認してください：
- **Docker** と **Docker Compose**（最新安定版）
- バージョン管理用 **Git**
- **Make**（オプション、便利スクリプト用）

### ローカル開発環境のセットアップ

```bash
# 1. リポジトリをクローン
git clone https://github.com/Be114/LLM_TOPIX.git
cd LLM_TOPIX

# 2. スクリプトを実行可能にする
chmod +x scripts/*.sh

# 3. 開発環境をセットアップ（データベースの初期化、依存関係のインストール）
./scripts/setup.sh

# 4. 開発モードですべてのサービスを開始
docker-compose up -d

# 5. テストを実行してセットアップを確認
./scripts/test.sh

# 6. ログを表示（オプション）
docker-compose logs -f
```

### 開発スクリプト

プロジェクトには一般的なタスク用の便利な開発スクリプトが含まれています：

```bash
# 開発環境を開始
./scripts/setup.sh

# すべてのテストを実行（バックエンド + フロントエンド）
./scripts/test.sh

# 特定のテストスイートを実行
./scripts/test.sh backend    # バックエンドテストのみ
./scripts/test.sh frontend   # フロントエンドテストのみ
./scripts/test.sh lint       # コード品質チェック

# 開発サーバー管理
docker-compose up -d         # すべてのサービスを開始
docker-compose down          # すべてのサービスを停止
docker-compose restart      # サービスを再起動
```

### アクセスポイント

セットアップ完了後、以下でアプリケーションにアクセスできます：

- **🌐 フロントエンドアプリケーション**: http://localhost:3000
- **⚡ バックエンドAPI**: http://localhost:5000
- **💚 ヘルスチェック**: http://localhost:5000/health
- **📰 最新記事API**: http://localhost:5000/api/articles/latest
- **📊 APIドキュメント**: http://localhost:5000/docs（利用可能な場合）

## 🏗 プロジェクトアーキテクチャ

```
LLM_TOPIX/
├── 🗄️ backend/                    # Flask APIサーバー
│   ├── app/
│   │   ├── 📊 models/              # SQLAlchemyデータモデル
│   │   │   ├── article.py          # 最適化されたクエリ付き記事モデル
│   │   │   └── __init__.py
│   │   ├── 🔧 services/            # ビジネスロジック層
│   │   │   ├── article_service.py  # パフォーマンス監視付き記事操作
│   │   │   ├── formatters.py       # データフォーマットユーティリティ
│   │   │   └── __init__.py
│   │   ├── 🛤️ routes/              # APIエンドポイント定義
│   │   │   ├── articles.py         # 記事関連エンドポイント
│   │   │   └── __init__.py
│   │   ├── ⚙️ config/              # 設定管理
│   │   │   ├── constants.py        # アプリケーション定数
│   │   │   ├── database.py         # データベース設定
│   │   │   └── __init__.py
│   │   ├── 🔧 utils/               # ユーティリティ関数
│   │   │   ├── response_helpers.py # 標準化されたAPIレスポンス
│   │   │   └── __init__.py
│   │   ├── exceptions.py           # カスタム例外階層
│   │   └── app.py                  # アプリケーションファクトリ
│   ├── 🧪 tests/                   # バックエンドテストスイート
│   │   ├── test_api_endpoints.py   # 統合テスト
│   │   ├── test_article_service.py # ユニットテスト
│   │   └── __init__.py
│   ├── pyproject.toml              # Poetry設定
│   └── Dockerfile                  # バックエンドコンテナ定義
├── 🎨 frontend/                    # Next.jsアプリケーション
│   ├── src/
│   │   ├── 🧩 components/          # Reactコンポーネント
│   │   │   ├── ArticleCard.tsx     # 記事表示コンポーネント
│   │   │   ├── ArticleCard.module.css
│   │   │   └── __tests__/          # コンポーネントテスト
│   │   │       └── ArticleCard.test.tsx
│   │   ├── 📄 pages/               # Next.jsページ（自動ルーティング）
│   │   ├── 🏷️ types/               # TypeScript型定義
│   │   │   └── article.ts          # 記事関連型とインターフェース
│   │   └── 🔧 utils/               # フロントエンドユーティリティ
│   ├── 🧪 tests/                   # フロントエンドテスト設定
│   ├── package.json                # npm設定
│   ├── next.config.js              # Next.js設定
│   ├── tsconfig.json               # TypeScript設定
│   ├── jest.setup.js               # Jestテストセットアップ
│   └── Dockerfile                  # フロントエンドコンテナ定義
├── 🗃️ database/                    # データベーススキーマとマイグレーション
│   └── init.sql                    # 初期データベーススキーマ
├── 📜 scripts/                     # 開発・デプロイスクリプト
│   ├── setup.sh                    # 環境セットアップ
│   └── test.sh                     # テスト実行
├── 🐳 docker-compose.yml           # マルチサービスコンテナオーケストレーション
├── 📖 CLAUDE.md                    # 開発憲章とガイドライン
└── 📝 README.md                    # このファイル
```

## 📡 APIドキュメント

私たちのAPIは、一貫したレスポンス形式と包括的なエラーハンドリングによるRESTful原則に従っています。

### 基本情報
- **ベースURL**: `http://localhost:5000/api`
- **レスポンス形式**: JSON
- **認証**: 現在のエンドポイントには不要
- **レート制限**: 未実装（フェーズ2）

### コアエンドポイント

#### `GET /api/articles/latest`
最新5件のLLMおよびAIニュース記事を取得します。

**パラメータ**: なし

**成功レスポンス** (200):
```json
[
  {
    "id": 1,
    "title": "速報: GPT-5アーキテクチャが公開",
    "summary_truncated": "OpenAIが最新モデルで革命的なアーキテクチャ改善を発表、強化された推論機能を特徴として...",
    "published_at": "2024-01-15T10:30:00Z",
    "source_url": "https://example.com/gpt5-architecture"
  },
  {
    "id": 2,
    "title": "GoogleがGemini Ultra 2.0を発表",
    "summary_truncated": "Googleの最新マルチモーダルAIモデルは、コード生成と数学において大幅な改善を示す...",
    "published_at": "2024-01-14T15:45:00Z",
    "source_url": "https://example.com/gemini-ultra-2"
  }
  // ... 3つの記事が続く
]
```

**エラーレスポンス**:
- **503 Service Unavailable**: データベース接続問題
  ```json
  {
    "error": "Database service unavailable",
    "message": "Please try again later"
  }
  ```
- **500 Internal Server Error**: 予期しないサーバーエラー
  ```json
  {
    "error": "Internal server error",
    "message": "An unexpected error occurred"
  }
  ```

#### `GET /health`
サービス可用性監視用のヘルスチェックエンドポイント。

**成功レスポンス** (200):
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "services": {
    "database": "connected",
    "api": "operational"
  }
}
```

### レスポンス標準

すべてのAPIレスポンスは一貫したフォーマットに従います：

- **成功レスポンス**: 直接データまたは適切な構造にラップ
- **エラーレスポンス**: エラータイプ、ユーザーフレンドリーなメッセージ、関連詳細を含む
- **HTTPステータスコード**: セマンティックで一貫した使用
- **タイムスタンプ**: ISO 8601形式（UTC）
- **パフォーマンス**: すべてのエンドポイントで50ms未満のレスポンス時間を目標

## 🧪 テスト

私たちのテスト戦略は、すべての層にわたって包括的なカバレッジを持つテスト駆動開発（TDD）原則に従っています。

### テスト哲学

完全なTDDサイクルを実装しています：
1. **🔴 RED**: 望ましい機能を記述する失敗テストを書く
2. **🟢 GREEN**: テストを通すための最小限のコードを実装する
3. **🔵 REFACTOR**: テストカバレッジを維持しながらコード品質を向上させる

### テストの実行

```bash
# 完全なテストスイートを実行
./scripts/test.sh

# バックエンドテストのみ（PyTest）
./scripts/test.sh backend

# フロントエンドテストのみ（Jest）
./scripts/test.sh frontend

# コード品質とリンティング
./scripts/test.sh lint

# カバレッジレポート
./scripts/test.sh coverage
```

### テストカバレッジ要件

- **最小カバレッジ**: すべてのモジュールで90%
- **ユニットテスト**: すべてのビジネスロジックメソッドとコンポーネント
- **統合テスト**: APIエンドポイントとデータベースインタラクション
- **パフォーマンステスト**: レスポンス時間検証（バックエンド50ms未満、フロントエンド16ms未満）
- **アクセシビリティテスト**: WCAG 2.1 AA準拠検証

### テスト構成

#### バックエンドテスト（PyTest）
```python
# テスト構造の例
class TestArticleService:
    def test_get_latest_articles_returns_five_articles(self):
        """正しい記事数が返されることを確認。"""
        
    def test_get_latest_articles_performance_requirement(self):
        """レスポンス時間が50ms未満であることを確認。"""
        
    def test_get_latest_articles_handles_database_error(self):
        """適切なエラーハンドリングをテスト。"""
```

#### フロントエンドテスト（Jest + React Testing Library）
```typescript
// コンポーネントテストの例
describe('ArticleCard Component', () => {
  describe('UI表示', () => {
    test('記事情報が正しく表示される', () => {
      // テスト実装
    });
  });
  
  describe('アクセシビリティ', () => {
    test('適切なARIA属性を持つ', () => {
      // アクセシビリティ検証
    });
  });
  
  describe('パフォーマンス', () => {
    test('16ms予算内でレンダリングされる', () => {
      // パフォーマンス検証
    });
  });
});
```

## 🚀 パフォーマンス要件

私たちのプラットフォームは、パフォーマンスをファーストクラスの関心事として構築されています：

### バックエンドパフォーマンス
- **🎯 APIレスポンス時間**: データ取得エンドポイントで50ms未満
- **📊 データベースクエリ**: 適切なインデックスによる10ms未満の実行時間
- **📈 監視**: 自動警告付きの組み込みパフォーマンス追跡
- **🔍 プロファイリング**: すべてのサービスメソッドの実行時間ログ

### フロントエンドパフォーマンス
- **⚡ UIインタラクション**: スムーズな60fpsインタラクションのため16ms未満
- **📦 バンドルサイズ**: 圧縮JavaScript 1MB未満
- **🖼️ 画像最適化**: 遅延読み込みとレスポンシブ画像
- **♿ アクセシビリティ**: スクリーンリーダーとキーボードナビゲーション用に最適化

### パフォーマンス監視

```python
# パフォーマンス監視の例（バックエンド）
def get_latest_articles(self) -> List[Dict[str, Any]]:
    start_time = time.time()
    try:
        # ビジネスロジック
        return articles
    finally:
        execution_time = (time.time() - start_time) * 1000
        if execution_time > PERFORMANCE_THRESHOLD_MS:
            logger.warning(f"遅い操作: {execution_time:.2f}ms")
```

## 🔒 セキュリティ

セキュリティは、複数の保護層を持つアーキテクチャ全体に統合されています：

### 入力検証
- **バックエンド**: Marshmallowスキーマを使用した包括的検証
- **フロントエンド**: サーバーサイド検証によるクライアントサイド検証
- **データベース**: SQLインジェクションを防ぐパラメータ化クエリ

### データ保護
- **XSS防止**: HTMLコンテンツ用のReact組み込みエスケープ + DOMPurify
- **CSRF保護**: 状態変更操作用のトークンベース検証
- **CORS設定**: 厳格なオリジンとメソッド制限

### 設定セキュリティ
- **環境変数**: すべての機密設定を外部化
- **秘密管理**: ハードコードされた認証情報やAPIキーなし
- **データベースセキュリティ**: 接続暗号化とアクセス制御

### セキュリティヘッダー
```python
# セキュリティ設定の例
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

## 🤝 貢献

貢献を歓迎します！確立された開発ワークフローに従ってください：

### 開発ワークフロー

1. **📋 Issues**: Issue の作成または取得から開始
2. **🌿 ブランチ**: 命名規則に従ってフィーチャーブランチを作成
3. **🔴 TDD プロセス**: テストを最初に書き、次に実装
4. **✅ 品質チェック**: すべてのテストが通り、コード品質基準を満たすことを確認
5. **📝 プルリクエスト**: 詳細な説明とテストカバレッジ付きでPRを提出
6. **👀 レビュー**: チームメンバーによるコードレビュー
7. **🚀 マージ**: 承認とCI/CD検証後にマージ

### ブランチ命名規則
- `feat/description-of-feature` - 新機能
- `fix/description-of-bug` - バグ修正
- `refactor/description-of-refactor` - コード改善
- `docs/description-of-docs` - ドキュメント更新
- `chore/description-of-chore` - メンテナンスタスク

### コミットメッセージ形式
[Conventional Commits](https://www.conventionalcommits.org/) を使用します：

```
type(scope): description

[optional body]

[optional footer(s)]
```

**例**:
```bash
feat(articles): add pagination support to latest articles API
fix(frontend): resolve memory leak in ArticleCard component
docs(readme): update API documentation with new endpoints
```

### プルリクエストチェックリスト
- [ ] すべてのテストが通る（`./scripts/test.sh`）
- [ ] コードカバレッジが90%以上の閾値を維持
- [ ] パフォーマンス要件を満たす（バックエンド50ms未満、フロントエンド16ms未満）
- [ ] [CLAUDE.md](CLAUDE.md) のスタイルガイドラインに従う
- [ ] 新機能のドキュメントを更新
- [ ] 新しいセキュリティ脆弱性を導入しない
- [ ] アクセシビリティ要件を維持（WCAG 2.1 AA）

### 開発ガイドライン

包括的な開発標準、アーキテクチャ決定、ベストプラクティスについては、私たちの [**開発憲章（CLAUDE.md）**](CLAUDE.md) を参照してください。このドキュメントでは以下をカバーしています：

- 📝 コーディング標準と命名規則
- 🏗️ アーキテクチャと設計原則
- 🔒 セキュリティガイドラインとベストプラクティス
- 🧪 テスト戦略と要件
- 📊 パフォーマンス最適化技術
- 🔄 Git ワークフローとブランチ管理
- 📦 依存関係管理プロトコル

## 📄 ライセンス

このプロジェクトは [MIT License](LICENSE) の下でライセンスされています - 詳細はLICENSEファイルを参照してください。

## 🙏 謝辞

- テスト駆動開発原則で ❤️ を込めて構築
- 最新のWeb技術とAIイノベーションによる動力
- WCAG 2.1 AA基準に基づくアクセシビリティガイドライン
- Google Web Vitals にインスパイアされたパフォーマンスベンチマーク

---

**🚀 LLMとAIニュースの未来を探索する準備はできましたか？**

[始める](#クイックスタート) | [ライブデモを見る](http://localhost:3000) | [APIドキュメント](#apiドキュメント) | [貢献ガイドライン](#貢献)

---

<div align="center">

**テスト駆動開発原則で構築**  
*[Claude Code](https://claude.ai/code) で生成*

</div>