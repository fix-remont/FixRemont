#!/bin/bash

read -r message

pnpm format >dev/null 2>&1
git add .
git commit -m "$message"