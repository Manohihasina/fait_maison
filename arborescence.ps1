
$directories = @(
    "app",
    "app\core",
    "app\models",
    "app\schemas",
    "app\repositories",
    "app\services",
    "app\api",
    "app\api\routes",
    "app\utils",
    "alembic",
    "alembic\versions",
    "tests"
)

foreach ($directory in $directories) {
    New-Item -ItemType Directory -Path $directory -Force | Out-Null
}

$files = @(
    "app\__init__.py",
    "app\main.py",

    "app\core\__init__.py",
    "app\core\config.py",
    "app\core\database.py",
    "app\core\security.py",
    "app\core\dependencies.py",

    "app\models\__init__.py",
    "app\models\role.py",
    "app\models\user.py",
    "app\models\product_category.py",
    "app\models\product.py",
    "app\models\production.py",
    "app\models\status.py",
    "app\models\transaction.py",
    "app\models\transaction_history.py",
    "app\models\expense.py",
    "app\models\expense_history.py",
    "app\models\stock.py",
    "app\models\type_mouvement.py",
    "app\models\stock_history.py",

    "app\schemas\auth.py",
    "app\schemas\user.py",
    "app\schemas\product.py",
    "app\schemas\production.py",
    "app\schemas\transaction.py",
    "app\schemas\expense.py",
    "app\schemas\stock.py",
    "app\schemas\history.py",
    "app\schemas\dashboard.py",

    "app\repositories\user_repository.py",
    "app\repositories\product_repository.py",
    "app\repositories\production_repository.py",
    "app\repositories\transaction_repository.py",
    "app\repositories\expense_repository.py",
    "app\repositories\stock_repository.py",
    "app\repositories\history_repository.py",

    "app\services\auth_service.py",
    "app\services\user_service.py",
    "app\services\product_service.py",
    "app\services\production_service.py",
    "app\services\transaction_service.py",
    "app\services\expense_service.py",
    "app\services\stock_service.py",
    "app\services\history_service.py",
    "app\services\dashboard_service.py",

    "app\api\__init__.py",
    "app\api\router.py",

    "app\api\routes\__init__.py",
    "app\api\routes\auth.py",
    "app\api\routes\users.py",
    "app\api\routes\products.py",
    "app\api\routes\production.py",
    "app\api\routes\transactions.py",
    "app\api\routes\expenses.py",
    "app\api\routes\stock.py",
    "app\api\routes\history.py",
    "app\api\routes\dashboard.py",

    "app\utils\__init__.py",
    "app\utils\enums.py",
    "app\utils\helpers.py",

    "tests\__init__.py",
    ".env",
    ".env.example",
    ".gitignore"
)

foreach ($file in $files) {
    if (-not (Test-Path $file)) {
        New-Item -ItemType File -Path $file -Force | Out-Null
    }
}

Write-Host "Arborescence créée avec succès !" -ForegroundColor Green