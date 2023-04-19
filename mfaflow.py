# mfaflow.py
from graphviz import Digraph

dot = Digraph('mfa_flow', format='png')

dot.attr(rankdir='TB', size='8,5')

dot.attr('node', shape='rectangle')
dot.node('A', 'Premier Success Entitlement')

dot.attr('node', shape='diamond')
dot.node('B', 'Case Queue')

dot.attr('node', shape='rectangle')
dot.node('C', 'CSM will be assigned Case')
dot.node('D', 'CSM will reach out to the customer')
dot.node('E', 'CSM will discuss MFA with the Cloud Admin at the BSP')
dot.node('F', 'CSM will review the form with the Cloud Admin at the BSP')

dot.node('G', 'APM will be assigned Case')
dot.node('H', 'APM will reach out to the customer')
dot.node('I', 'APM will discuss MFA with the Cloud Admin at the BSP')
dot.node('J', 'APM will review the form with the Cloud Admin at the BSP')

dot.attr('node', shape='diamond')
dot.node('K', 'Does the BSP use third party for cloud support?')
dot.node('L', 'Does the BSP use third party for cloud support?')

dot.attr('node', shape='rectangle')
dot.node('M', 'CSM Updates the Case that 3rd Party is Used')
dot.node('N', 'CSM Open Question Mark Box Yellow')
dot.node('O', 'APM Updates the Case that 3rd Party is Used')
dot.node('P', 'APM Open Question Mark Box Yellow')

dot.attr('node', shape='rectangle')
dot.node('Q', 'CSM Will get the date the BSP will fill out the form and update the case')
dot.node('R', 'APM Will get the date the BSP will fill out the form and update the case')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FK', 'BG', 'GH', 'HI', 'IJ', 'JL'])
dot.edges(['KM', 'MN', 'KO', 'OP'])
dot.edges(['KQ', 'LQ', 'LR'])

dot.render('mfa_flow', view=True)