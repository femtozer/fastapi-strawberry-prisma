-- CreateEnum
CREATE TYPE "Priority" AS ENUM ('low', 'medium', 'high');

-- CreateTable
CREATE TABLE "Todo" (
    "id" VARCHAR(255) NOT NULL,
    "title" VARCHAR(255),
    "description" VARCHAR(255),
    "priority" "Priority",

    CONSTRAINT "Todo_pkey" PRIMARY KEY ("id")
);
