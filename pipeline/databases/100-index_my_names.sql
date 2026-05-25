-- 100-index_my_names.sql
-- Create index on first letter of name
CREATE INDEX idx_name_first ON names(name(1));
