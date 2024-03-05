interface InputProps {
  value: string | number | undefined 
  type: 'text' | 'number' | 'email' | 'password' 
  label: string 
  onChange: (value: string | number) => void 
}

export default InputProps 
