<h2><a href="https://leetcode.com/problems/consecutive-numbers/">180. Consecutive Numbers</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi" style="user-select: auto;"><a class="sql-schema-link__3cEg" style="user-select: auto;">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2" style="user-select: auto;"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" style="user-select: auto;"></path></svg></a></div><div style="user-select: auto;"><p style="user-select: auto;">Table: <code style="user-select: auto;">Logs</code></p>

<pre style="user-select: auto;">+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key for this table.
</pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;">Write an SQL query to find all numbers that appear at least three times consecutively.</p>

<p style="user-select: auto;">Return the result table in <strong style="user-select: auto;">any order</strong>.</p>

<p style="user-select: auto;">The query result format is in the following example.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
<strong style="user-select: auto;">Output:</strong> 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
<strong style="user-select: auto;">Explanation:</strong> 1 is the only number that appears consecutively for at least three times.
</pre>
</div>