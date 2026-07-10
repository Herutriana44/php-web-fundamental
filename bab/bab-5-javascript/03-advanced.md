# Bab 5: JavaScript Advanced — ES6+, Modules, Debugging, Testing

Setelah menguasai JavaScript dasar, langkah berikutnya adalah ES6+ features, modular code, debugging, dan testing — skill essential untuk production JavaScript applications.

## 1. ES6+ Features

### Arrow Functions & Short Syntax
```javascript
// ES5
const add = function(a, b) { return a + b; };

// ES6 arrow function
const add = (a, b) => a + b;

// Multiple lines: use braces
const process = (data) => {
    console.log("Processing...");
    return data * 2;
};

// Single parameter: parentheses optional
const double = x => x * 2;
```

### Destructuring
```javascript
// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first, second, rest);  // 1, 2, [3, 4, 5]

// Object destructuring
const { name, email, age = 25 } = user;  // age defaults to 25

// Nested destructuring
const { user: { profile: { avatar } } } = data;

// Function parameter destructuring
const greet = ({ name, title = "user" }) => {
    console.log(`Hello ${name}, ${title}!`);
};
```

### Template Literals
```javascript
const name = "Alice";
const age = 30;

// Template literals (backticks)
const message = `Hello ${name}, you are ${age} years old`;

// Multiline strings
const html = `
    <div class="card">
        <h2>${name}</h2>
        <p>Age: ${age}</p>
    </div>
`;

// Expressions inside ${}
const result = `Result: ${2 + 3 * 5}`;
```

### Spread & Rest Operators
```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Spread operator (copy arrays)
const combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// Rest parameters (gather remaining args)
const sum = (...numbers) => numbers.reduce((a, b) => a + b, 0);
sum(1, 2, 3, 4);  // 10

// Spread in objects
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 };  // { a: 1, b: 2, c: 3 }
```

### Const & Let (vs Var)
```javascript
// var: function-scoped, can redeclare (problematic)
var x = 1;
var x = 2;  // OK

// let: block-scoped, cannot redeclare
let y = 1;
// let y = 2;  // Error!
if (true) {
    let y = 3;  // Different y (block scope)
}

// const: block-scoped, immutable reference
const PI = 3.14;
// PI = 3.15;  // Error!

// const object: reference is immutable, but properties can change
const user = { name: "Alice" };
user.name = "Bob";  // OK
// user = {};  // Error!
```

### Default Parameters & Enhancements
```javascript
// Default parameters
const greet = (name = "Guest") => `Hello ${name}`;

// Object shorthand
const name = "Bob";
const age = 25;
const user = { name, age };  // { name: "Bob", age: 25 }

// Computed property names
const prop = "email";
const obj = { [prop]: "test@example.com" };  // { email: "test@example.com" }
```

## 2. Modules (Import/Export)

### Named Exports
```javascript
// math.js
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;

// main.js
import { add, multiply } from './math.js';
console.log(add(2, 3));  // 5

// Import all
import * as math from './math.js';
console.log(math.add(2, 3));
```

### Default Export
```javascript
// logger.js
const log = (msg) => console.log(`[LOG] ${msg}`);
export default log;

// main.js
import log from './logger.js';
log("Hello");
```

### Mixed Exports
```javascript
// utils.js
export const helper = () => {};
export default function main() {}

// main.js
import main, { helper } from './utils.js';
```

## 3. Debugging Techniques

### Console Methods
```javascript
console.log("Info");
console.warn("Warning");
console.error("Error");

// Table for structured data
console.table([
    { name: "Alice", age: 30 },
    { name: "Bob", age: 25 }
]);

// Grouping
console.group("Group 1");
console.log("Item 1");
console.log("Item 2");
console.groupEnd();

// Timing
console.time("fetch");
// ... code ...
console.timeEnd("fetch");
```

### Browser DevTools
```javascript
// Debugger statement (pauses execution in DevTools)
debugger;

// Conditional breakpoints: right-click breakpoint in DevTools
// Edit breakpoint condition: e.g., x > 5
```

### Try-Catch Debugging
```javascript
try {
    riskFunction();
} catch (error) {
    console.error("Error details:", error.message);
    console.error("Stack:", error.stack);
    // Log to monitoring service
}
```

## 4. Testing Basics (Jest)

### Installation
```bash
npm install --save-dev jest
npm test
```

### Simple Test
```javascript
// math.test.js
import { add } from './math.js';

describe('Math utilities', () => {
    test('add should sum two numbers', () => {
        expect(add(2, 3)).toBe(5);
    });

    test('add should handle negative numbers', () => {
        expect(add(-2, 3)).toBe(1);
    });
});
```

### Testing Assertions
```javascript
expect(value).toBe(5);              // === equality
expect(value).toEqual([1, 2, 3]);   // deep equality
expect(value).toContain(2);         // array contains
expect(fn).toThrow();               // throws error
expect(promise).resolves.toBe(5);   // async resolves
```

### Mocking
```javascript
jest.mock('./api');

test('fetch user', async () => {
    API.getUser.mockResolvedValue({ id: 1, name: 'Alice' });
    const user = await getUser(1);
    expect(user.name).toBe('Alice');
});
```

## 5. Best Practices

- Use `const` by default, `let` if reassigning, never `var`
- Use arrow functions for most cases (except methods needing `this`)
- Module imports/exports for code organization
- Use async/await instead of `.then()` chains
- Test critical functions and edge cases
- Use linting (ESLint) to catch common mistakes
- Type safety: consider TypeScript or JSDoc
